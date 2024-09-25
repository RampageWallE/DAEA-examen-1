from flask import Flask, request, jsonify
import requests
import math
from collections import defaultdict

app = Flask(__name__)

# URL de la API de .NET
API_URL = "http://api:8080/api/user/all"  # Ajusta según tu configuración

def compute_tf(documents):
    tf_list = []
    for doc in documents:
        tf_dict = defaultdict(float)
        words = doc.split()
        total_words = len(words)
        for word in words:
            tf_dict[word] += 1
        # Normalizar TF
        for word in tf_dict:
            tf_dict[word] /= total_words
        tf_list.append(tf_dict)
    return tf_list

def compute_idf(documents):
    idf_dict = defaultdict(float)
    total_docs = len(documents)

    for doc in documents:
        words = set(doc.split())
        for word in words:
            idf_dict[word] += 1

    # Calcular IDF
    for word in idf_dict:
        idf_dict[word] = math.log(total_docs / (1 + idf_dict[word]))
    return idf_dict

def compute_tfidf(documents):
    tf_list = compute_tf(documents)
    idf_dict = compute_idf(documents)

    tfidf_list = []
    for tf_dict in tf_list:
        tfidf_dict = {}
        for word, tf in tf_dict.items():
            tfidf_dict[word] = tf * idf_dict[word]
        tfidf_list.append(tfidf_dict)
    return tfidf_list

@app.route('/search', methods=['GET'])
def search_users():
    query = request.args.get('query', '').lower()  # Convertir la consulta a minúsculas

    # Obtener usuarios desde la API
    response = requests.get(API_URL)
    users = response.json()

    # Preparar los datos para TF-IDF
    documents = []
    for user in users:
        # Concatenar campos relevantes y convertir a minúsculas
        full_text = f"{user['name']} {user['lastname']} {user['email']} {user['address']} {user['phone']} {user['occupation']}".lower()
        documents.append(full_text)

    # Calcular TF-IDF
    tfidf_documents = compute_tfidf(documents)

    # Transformar la consulta a un vector TF-IDF
    query_tf = compute_tf([query])
    query_idf = compute_idf(documents)
    query_tfidf = {word: tf * query_idf[word] for word, tf in query_tf[0].items()}

    # Calcular similitudes (simple dot product)
    results = []
    for i, user in enumerate(users):
        score = sum(query_tfidf.get(word, 0) * tfidf_documents[i].get(word, 0) for word in query_tfidf)
        if score > 0:  # Si hay alguna coincidencia significativa
            results.append({"user": user, "score": score})

    # Ordenar resultados por puntuación
    results.sort(key=lambda x: x['score'], reverse=True)

    return jsonify([result['user'] for result in results])

if __name__ == '__main__':
    app.run(debug=True)

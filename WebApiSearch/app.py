from flask import Flask, request, jsonify
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# URL de la API de .NET
API_URL = "http://api:8080/api/user/all"  # Ajusta según tu configuración

@app.route('/search', methods=['GET'])
def search_users():
    query = request.args.get('query', '')

    # Obtener usuarios desde la API
    response = requests.get(API_URL)
    users = response.json()

    # Preparar los datos para TF-IDF
    documents = []
    for user in users:
        # Concatenar campos relevantes
        full_text = f"{user['name']} {user['lastname']} {user['email']} {user['address']} {user['phone']} {user['occupation']}"
        documents.append(full_text)

    # Crear la matriz TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Transformar la consulta
    query_vector = vectorizer.transform([query])

    # Calcular la similitud
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # Obtener los índices de los usuarios ordenados por similitud
    similar_indices = similarity_scores.argsort()[::-1]

    # Filtrar resultados
    results = [users[i] for i in similar_indices if similarity_scores[i] > 0]

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

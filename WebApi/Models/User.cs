using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace WebApi.Models
{
    public class User
    {
        [BsonId] // Este es el identificador del documento en MongoDB
        [BsonRepresentation(BsonType.ObjectId)] // Mapear el ObjectId de MongoDB
        public string id { get; set; }

        [BsonElement("name")] // Corresponde al campo 'name' en MongoDB
        public string name { get; set; }

        [BsonElement("lastname")] // Corresponde al campo 'lastname' en MongoDB
        public string lastname { get; set; }

        [BsonElement("email")] // Corresponde al campo 'email' en MongoDB
        public string email { get; set; }

        [BsonElement("age")] // Corresponde al campo 'age' en MongoDB
        public int age { get; set; }

        [BsonElement("address")] // Corresponde al campo 'address' en MongoDB
        public string address { get; set; }

        [BsonElement("phone")] // Corresponde al campo 'phone' en MongoDB
        public string phone { get; set; }

        [BsonElement("gender")] // Corresponde al campo 'gender' en MongoDB
        public string gender { get; set; }

        [BsonElement("occupation")] // Corresponde al campo 'occupation' en MongoDB
        public string occupation { get; set; }

        [BsonElement("created_at")] // Corresponde al campo 'created_at' en MongoDB
        public DateTime created_at { get; set; }
    }
};
using Microsoft.AspNetCore.Mvc;
using MongoDB.Driver;
using WebApi.Models;

namespace WebApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class UserController : ControllerBase
    {

        private readonly ILogger<UserController> _logger;
        private readonly HttpClient _httpClient;
        private IMongoCollection<User> _usersCollection;

        public UserController(ILogger<UserController> logger, HttpClient httpClient, IMongoClient mongoClient)
        {
            _logger = logger;
            _httpClient = httpClient; // Para la API externa

            // Inicializamos la base de datos y la colección 'Users' en MongoDB
            var database = mongoClient.GetDatabase("WebApi"); // Ajusta el nombre de tu BD
            _usersCollection = database.GetCollection<User>("User");
        }


        [HttpGet("all", Name = "GetMongoUsers")]
        public async Task<IActionResult> GetMongoUsers()
        {
            try
            {
                // Obtenemos todos los usuarios de la colección
                var users = await _usersCollection.Find(_ => true).ToListAsync();

                // Devolvemos los usuarios como respuesta JSON
                return Ok(users);
            }
            catch (Exception ex)
            {
                // Manejo de error en caso de fallo en la conexión con MongoDB
                return Problem($"Error al conectar con la base de datos: {ex.Message}");
            }
        }

        // Nuevo endpoint para obtener usuarios de la API externa
        [HttpGet("all2", Name = "GetUsers")]
        public async Task<IActionResult> GetUsers()
        {
            // URL de la API RandomUser
            var apiUrl = "https://randomuser.me/api/?results=1";

            try
            {
                // Realiza una solicitud GET a la API y obtiene el contenido como string
                var response = await _httpClient.GetStringAsync(apiUrl);

                // Devuelve el contenido JSON tal como fue recibido
                return Content(response, "application/json");
            }
            catch (HttpRequestException ex)
            {
                // Manejo de error en caso de fallo en la solicitud
                return Problem($"Error al conectar con la API externa: {ex.Message}");
            }
        }
    }
}

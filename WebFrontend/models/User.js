const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    name: { type: String, required: true },
    lastname: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    age: { type: Number, required: true },
    address: { type: String, required: true },
    phone: { type: String, required: true },
    gender: { type: String, required: true },
    occupation: { type: String, required: true },
    created_at: { type: Date, default: Date.now }
});

// Eliminar el campo 'id' ya que MongoDB genera su propio ObjectId
const User = mongoose.model('User', userSchema);

module.exports = User;
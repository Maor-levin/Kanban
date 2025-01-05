// src/Auth/Login.js
import React, { useState } from 'react';
import axiosInstance from '../Utils/axiosInstance'; // Updated import
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../Context/AuthContext';
import './auth.css'; // Optional: Styles specific to Auth

function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post('/users/login', {
        username,
        password,
      });
      login(response.data.access_token);
      navigate('/boards');
    } catch (error) {
      console.error(error);
      setMessage(error.response?.data?.detail || 'Login failed');
    }
  };

  return (
    <div className="auth-container">
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>
      {message && <p className="error">{message}</p>}
      <p>
        Don't have an account? <Link to="/register">Register here</Link>
      </p>
    </div>
  );
}

export default Login;

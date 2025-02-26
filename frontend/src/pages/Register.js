import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../api/axiosConfig";
import "../styles/App.css";

function Register() {
  const [formData, setFormData] = useState({ username: "", password: "" });
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Adjust if your register endpoint differs
      await api.post("/register", formData);
      // After successful registration, navigate to login
      navigate("/login");
    } catch (err) {
      setErrorMessage("Registration failed. User may already exist.");
    }
  };

  return (
    <div className="login-page">
      <h2>Register</h2>
      {errorMessage && <p className="error">{errorMessage}</p>}
      <form onSubmit={handleSubmit} className="login-form">
        <div>
          <label>Username</label>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Password</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Register</button>
      </form>
      <p>
        Have an account? <Link to="/login">Login here</Link>.
      </p>
    </div>
  );
}

export default Register;

import React, { useContext, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../api/axiosConfig";
import { AuthContext } from "../Context/AuthContext";
import "../styles/App.css";

function Login() {
  const { setToken } = useContext(AuthContext);
  const [formData, setFormData] = useState({ username: "", password: "" });
  const navigate = useNavigate();
  const [errorMessage, setErrorMessage] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Adjust the endpoint name to match your FastAPI backend
      const res = await api.post("/login", formData);
      if (res.data.access_token) {
        setToken(res.data.access_token);
        navigate("/");
      }
    } catch (err) {
      setErrorMessage("Invalid credentials, please try again.");
    }
  };

  return (
    <div className="login-page">
      <h2>Login</h2>
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
        <button type="submit">Login</button>
      </form>
      <p>
        New user? <Link to="/register">Register here</Link>.
      </p>
    </div>
  );
}

export default Login;

// src/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from './Context/AuthContext';
import './Navbar.css'; // Optional: Styles specific to Navbar

function Navbar() {
  const { isAuthenticated, logout } = useAuth();

  const handleLogout = () => {
    logout();
  };

  return (
    <nav className="navbar">
      <h1>Kanban App</h1>
      <div>
        {isAuthenticated ? (
          <>
            <Link to="/boards">Boards</Link>
            <button onClick={handleLogout}>Logout</button>
          </>
        ) : (
          <>
            <Link to="/">Login</Link>
            <Link to="/register">Register</Link>
          </>
        )}
      </div>
    </nav>
  );
}

export default Navbar;

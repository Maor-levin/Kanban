import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Login from './Auth/Login';
import Register from './Auth/Register';
import BoardList from './Boards/BoardList';
import Board from './Boards/Board';
import ProtectedRoute from './ProtectedRoute';
import Navbar from './Navbar';
import './index.css'; // Ensure global styles are applied

function App() {
  return (
    <div className="App">
      <Navbar />
      <Routes>
        {/* Public Routes */}
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Protected Routes */}
        <Route
          path="/boards"
          element={
            <ProtectedRoute>
              <BoardList />
            </ProtectedRoute>
          }
        />
        <Route
          path="/boards/:id"
          element={
            <ProtectedRoute>
              <Board />
            </ProtectedRoute>
          }
        />

        {/* Redirect Unknown Routes to Login */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </div>
  );
}

export default App;

// src/Boards/BoardList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../config';
import { useAuth } from '../Context/AuthContext';
import { Link } from 'react-router-dom';
import './boards.css'; // Optional: Styles specific to Boards

function BoardList() {
  const { token, logout } = useAuth();
  const [boards, setBoards] = useState([]);
  const [newBoardName, setNewBoardName] = useState('');
  const [message, setMessage] = useState('');

  const fetchBoards = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/boards`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setBoards(response.data);
    } catch (error) {
      console.error(error);
      setMessage('Failed to fetch boards');
    }
  };

  useEffect(() => {
    fetchBoards();
    // eslint-disable-next-line
  }, []);

  const handleCreateBoard = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        `${API_BASE_URL}/api/boards`,
        { name: newBoardName },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setBoards([...boards, response.data]);
      setNewBoardName('');
      setMessage('Board created successfully');
    } catch (error) {
      console.error(error);
      setMessage('Failed to create board');
    }
  };

  const handleLogout = () => {
    logout();
  };

  return (
    <div className="board-list-container">
      <h2>Your Boards</h2>
      <ul>
        {boards.map((board) => (
          <li key={board.id}>
            <Link to={`/boards/${board.id}`}>{board.name}</Link>
          </li>
        ))}
      </ul>
      <form onSubmit={handleCreateBoard}>
        <input
          type="text"
          value={newBoardName}
          onChange={(e) => setNewBoardName(e.target.value)}
          placeholder="New Board Name"
          required
        />
        <button type="submit">Create Board</button>
      </form>
      {message && <p className="message">{message}</p>}
    </div>
  );
}

export default BoardList;

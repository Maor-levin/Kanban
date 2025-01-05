// src/Boards/Board.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../config';
import { useAuth } from '../Context/AuthContext';
import { useParams, Link } from 'react-router-dom';
import TaskList from '../Tasks/TaskList';
import './boards.css'; // Optional: Styles specific to Boards

function Board() {
  const { id } = useParams();
  const { token, logout } = useAuth();
  const [board, setBoard] = useState(null);
  const [tasks, setTasks] = useState([]);
  const [newTaskTitle, setNewTaskTitle] = useState('');
  const [message, setMessage] = useState('');

  const fetchBoard = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/boards`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      const foundBoard = response.data.find((b) => b.id === parseInt(id));
      setBoard(foundBoard);
    } catch (error) {
      console.error(error);
      setMessage('Failed to fetch board');
    }
  };

  const fetchTasks = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/tasks?board_id=${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setTasks(response.data);
    } catch (error) {
      console.error(error);
      setMessage('Failed to fetch tasks');
    }
  };

  useEffect(() => {
    fetchBoard();
    fetchTasks();
    // eslint-disable-next-line
  }, [id]);

  const handleCreateTask = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        `${API_BASE_URL}/api/tasks`,
        {
          title: newTaskTitle,
          status: 'To Do',
          board_id: parseInt(id),
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setTasks([...tasks, response.data]);
      setNewTaskTitle('');
      setMessage('Task created successfully');
    } catch (error) {
      console.error(error);
      setMessage('Failed to create task');
    }
  };

  const handleLogout = () => {
    logout();
  };

  if (!board) {
    return <p>Loading board...</p>;
  }

  return (
    <div className="board-container">
      <h2>{board.name}</h2>
      <div className="board-actions">
        <button onClick={handleLogout}>Logout</button>
        <Link to="/boards">Back to Boards</Link>
      </div>
      <TaskList tasks={tasks} setTasks={setTasks} boardId={id} />
      <form onSubmit={handleCreateTask}>
        <input
          type="text"
          value={newTaskTitle}
          onChange={(e) => setNewTaskTitle(e.target.value)}
          placeholder="New Task Title"
          required
        />
        <button type="submit">Add Task</button>
      </form>
      {message && <p className="message">{message}</p>}
    </div>
  );
}

export default Board;

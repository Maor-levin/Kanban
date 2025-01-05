// src/Tasks/Task.js
import React, { useState } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../config';
import { useAuth } from '../Context/AuthContext';
import './tasks.css'; // Optional: Styles specific to Tasks

function Task({ task, setTasks, boardId }) {
  const { token } = useAuth();
  const [isEditing, setIsEditing] = useState(false);
  const [newStatus, setNewStatus] = useState(task.status);
  const [message, setMessage] = useState('');

  const handleStatusChange = async () => {
    try {
      const response = await axios.put(
        `${API_BASE_URL}/api/tasks/${task.id}`,
        { status: newStatus },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setTasks((prevTasks) =>
        prevTasks.map((t) => (t.id === task.id ? response.data : t))
      );
      setIsEditing(false);
      setMessage('Status updated successfully');
    } catch (error) {
      console.error(error);
      setMessage('Failed to update status');
    }
  };

  const handleDelete = async () => {
    if (!window.confirm('Are you sure you want to delete this task?')) return;
    try {
      await axios.delete(`${API_BASE_URL}/api/tasks/${task.id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setTasks((prevTasks) => prevTasks.filter((t) => t.id !== task.id));
      setMessage('Task deleted successfully');
    } catch (error) {
      console.error(error);
      setMessage('Failed to delete task');
    }
  };

  return (
    <div className="task-container">
      <span>{task.title}</span>
      {isEditing ? (
        <div className="task-actions">
          <select value={newStatus} onChange={(e) => setNewStatus(e.target.value)}>
            <option value="To Do">To Do</option>
            <option value="In Progress">In Progress</option>
            <option value="Done">Done</option>
          </select>
          <button onClick={handleStatusChange}>Save</button>
          <button onClick={() => setIsEditing(false)}>Cancel</button>
        </div>
      ) : (
        <div className="task-actions">
          <span className="task-status">{task.status}</span>
          <button onClick={() => setIsEditing(true)}>Edit</button>
          <button onClick={handleDelete}>Delete</button>
        </div>
      )}
      {message && <p className="message">{message}</p>}
    </div>
  );
}

export default Task;

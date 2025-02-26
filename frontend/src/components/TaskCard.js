import React, { useState } from "react";
import api from "../api/axiosConfig";

function TaskCard({ task, boardId, tasks, setTasks }) {
  const [title, setTitle] = useState(task.title);
  const [isEditing, setIsEditing] = useState(false);

  const handleUpdate = async () => {
    try {
      const res = await api.put(`/boards/${boardId}/tasks/${task.id}`, {
        title,
      });
      // Update local tasks state
      const updatedTasks = tasks.map((t) => (t.id === task.id ? res.data : t));
      setTasks(updatedTasks);
      setIsEditing(false);
    } catch (error) {
      console.error("Error updating task", error);
    }
  };

  const handleDelete = async () => {
    try {
      await api.delete(`/boards/${boardId}/tasks/${task.id}`);
      setTasks(tasks.filter((t) => t.id !== task.id));
    } catch (error) {
      console.error("Error deleting task", error);
    }
  };

  return (
    <div className="task-card">
      {isEditing ? (
        <>
          <input value={title} onChange={(e) => setTitle(e.target.value)} />
          <button onClick={handleUpdate}>Save</button>
        </>
      ) : (
        <h4 onClick={() => setIsEditing(true)}>{title}</h4>
      )}
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
}

export default TaskCard;

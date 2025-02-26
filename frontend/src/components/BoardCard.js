import React, { useEffect, useState } from "react";
import api from "../api/axiosConfig";
import TaskCard from "./TaskCard";

function BoardCard({ board }) {
  const [tasks, setTasks] = useState([]);
  const [newTaskTitle, setNewTaskTitle] = useState("");

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const res = await api.get(`/boards/${board.id}/tasks`);
        setTasks(res.data);
      } catch (error) {
        console.error("Error fetching tasks for board", error);
      }
    };
    fetchTasks();
  }, [board.id]);

  const handleCreateTask = async () => {
    if (!newTaskTitle) return;
    try {
      const res = await api.post(`/boards/${board.id}/tasks`, {
        title: newTaskTitle,
      });
      setTasks([...tasks, res.data]);
      setNewTaskTitle("");
    } catch (error) {
      console.error("Error creating task", error);
    }
  };

  return (
    <div className="board-card">
      <h3>{board.title}</h3>
      <div className="task-input">
        <input
          type="text"
          placeholder="New Task"
          value={newTaskTitle}
          onChange={(e) => setNewTaskTitle(e.target.value)}
        />
        <button onClick={handleCreateTask}>Add Task</button>
      </div>
      <div className="tasks-container">
        {tasks.map((task) => (
          <TaskCard
            key={task.id}
            task={task}
            boardId={board.id}
            tasks={tasks}
            setTasks={setTasks}
          />
        ))}
      </div>
    </div>
  );
}

export default BoardCard;

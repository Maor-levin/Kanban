import React, { useContext, useEffect, useState } from "react";
import api from "../api/axiosConfig";
import { AuthContext } from "../Context/AuthContext";
import BoardCard from "../components/BoardCard";
import Navbar from "../components/Navbar";
import "../styles/App.css";

function Dashboard() {
  const { token } = useContext(AuthContext);
  const [boards, setBoards] = useState([]);
  const [newBoardTitle, setNewBoardTitle] = useState("");

  useEffect(() => {
    const fetchBoards = async () => {
      try {
        const res = await api.get("/boards");
        setBoards(res.data);
      } catch (error) {
        console.error("Error fetching boards", error);
      }
    };
    if (token) fetchBoards();
  }, [token]);

  const handleCreateBoard = async () => {
    if (!newBoardTitle) return;
    try {
      const res = await api.post("/boards", { title: newBoardTitle });
      setBoards([...boards, res.data]);
      setNewBoardTitle("");
    } catch (error) {
      console.error("Error creating board", error);
    }
  };

  return (
    <div className="dashboard">
      <Navbar />
      <div className="board-creation">
        <input
          type="text"
          placeholder="New Board Title"
          value={newBoardTitle}
          onChange={(e) => setNewBoardTitle(e.target.value)}
        />
        <button onClick={handleCreateBoard}>Create Board</button>
      </div>
      <div className="board-list">
        {boards.map((board) => (
          <BoardCard key={board.id} board={board} />
        ))}
      </div>
    </div>
  );
}

export default Dashboard;

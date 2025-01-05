// src/Tasks/TaskList.js
import React from 'react';
import Task from './Task';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import axios from 'axios';
import { API_BASE_URL } from '../config';
import { useAuth } from '../Context/AuthContext';
import './tasks.css'; // Optional: Styles specific to Tasks

function TaskList({ tasks, setTasks, boardId }) {
  const { token } = useAuth();

  const statuses = ['To Do', 'In Progress', 'Done'];

  const onDragEnd = async (result) => {
    const { destination, source, draggableId } = result;

    if (!destination) return;

    const sourceStatus = source.droppableId;
    const destStatus = destination.droppableId;

    if (sourceStatus === destStatus) return;

    try {
      const response = await axios.put(
        `${API_BASE_URL}/api/tasks/${draggableId}`,
        { status: destStatus },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setTasks((prevTasks) =>
        prevTasks.map((task) =>
          task.id === parseInt(draggableId) ? response.data : task
        )
      );
    } catch (error) {
      console.error(error);
      alert('Failed to update task status');
    }
  };

  return (
    <DragDropContext onDragEnd={onDragEnd}>
      <div className="task-list-container">
        {statuses.map((status) => (
          <Droppable droppableId={status} key={status}>
            {(provided) => (
              <div
                className="task-column"
                ref={provided.innerRef}
                {...provided.droppableProps}
              >
                <h3>{status}</h3>
                <ul>
                  {tasks
                    .filter((task) => task.status === status)
                    .map((task, index) => (
                      <Draggable
                        key={task.id}
                        draggableId={task.id.toString()}
                        index={index}
                      >
                        {(provided) => (
                          <li
                            className="task-item"
                            ref={provided.innerRef}
                            {...provided.draggableProps}
                            {...provided.dragHandleProps}
                          >
                            <Task task={task} setTasks={setTasks} boardId={boardId} />
                          </li>
                        )}
                      </Draggable>
                    ))}
                  {provided.placeholder}
                </ul>
              </div>
            )}
          </Droppable>
        ))}
      </div>
    </DragDropContext>
  );
}

export default TaskList;

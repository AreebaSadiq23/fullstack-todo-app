import React, { useState, useEffect } from 'react';
import './Dashboard.css'; // Will create this CSS file next

const Dashboard = () => {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [filter, setFilter] = useState('all'); // 'all', 'pending', 'active', 'completed'

  useEffect(() => {
    fetch('http://localhost:8000/tasks')
      .then(response => response.json())
      .then(data => setTasks(data));
  }, []);

  const addTask = () => {
    fetch('http://localhost:8000/tasks', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ title, description, status: 'pending' }), // New tasks are pending
    })
      .then(response => response.json())
      .then(data => {
        setTasks([...tasks, data]);
        setTitle('');
        setDescription('');
      });
  };

  const deleteTask = (id) => {
    fetch(`http://localhost:8000/tasks/${id}`, {
      method: 'DELETE',
    }).then(() => {
      setTasks(tasks.filter(task => task.id !== id));
    });
  };

  const toggleComplete = (id, currentStatus) => {
    // Backend expects 'complete' or 'incomplete'
    const newStatus = currentStatus === 'completed' ? 'incomplete' : 'completed';
    fetch(`http://localhost:8000/tasks/${id}/${newStatus}`, {
      method: 'PUT',
    })
      .then(response => response.json())
      .then(updatedTask => {
        setTasks(tasks.map(task => (task.id === id ? updatedTask : task)));
      });
  };

  // Filter tasks based on the current filter state
  const filteredTasks = tasks.filter(task => {
    if (filter === 'all') return true;
    if (filter === 'pending') return task.status === 'pending';
    if (filter === 'active') return task.status === 'active'; // Assuming 'active' is a possible status
    if (filter === 'completed') return task.status === 'completed';
    return true;
  });

  return (
    <div className="dashboard-page">
      <header className="dashboard-header">
        <h1>Your Productivity Dashboard</h1>
        <p>Manage your tasks efficiently, track your progress, and conquer your day.</p>
      </header>

      <div className="dashboard-content">
        <aside className="dashboard-sidebar">
          <h2>Task Filters</h2>
          <button onClick={() => setFilter('all')} className={filter === 'all' ? 'active-filter' : ''}>All Tasks</button>
          <button onClick={() => setFilter('pending')} className={filter === 'pending' ? 'active-filter' : ''}>Pending</button>
          <button onClick={() => setFilter('active')} className={filter === 'active' ? 'active-filter' : ''}>Active</button>
          <button onClick={() => setFilter('completed')} className={filter === 'completed' ? 'active-filter' : ''}>Completed</button>
        </aside>

        <main className="dashboard-main">
          <section className="task-input-section">
            <h2>Add New Task</h2>
            <div className="task-input-form">
              <input
                type="text"
                placeholder="Task Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
              />
              <textarea
                placeholder="Task Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
              ></textarea>
              <button onClick={addTask}>Add Task</button>
            </div>
          </section>

          <section className="task-list-section">
            <h2>{filter === 'all' ? 'All' : filter.charAt(0).toUpperCase() + filter.slice(1)} Tasks</h2>
            <div className="task-list-grid">
              {filteredTasks.length === 0 ? (
                <p className="no-tasks">No {filter} tasks yet!</p>
              ) : (
                filteredTasks.map(task => (
                  <div key={task.id} className={`task-card ${task.status}`}>
                    <h3>{task.title}</h3>
                    <p>{task.description}</p>
                    <div className="task-actions">
                      <button
                        onClick={() => toggleComplete(task.id, task.status)}
                        className={task.status === 'completed' ? 'btn-incomplete' : 'btn-complete'}
                      >
                        {task.status === 'completed' ? 'Mark Incomplete' : 'Mark Completed'}
                      </button>
                      <button onClick={() => deleteTask(task.id)} className="btn-delete">Delete</button>
                    </div>
                  </div>
                ))
              )}
            </div>
          </section>
        </main>
      </div>
    </div>
  );
};

export default Dashboard;

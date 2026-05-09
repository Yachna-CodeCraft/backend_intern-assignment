import { useState } from "react";
import axios from "axios";
import "./App.css";

export default function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [token, setToken] = useState("");

  const [task, setTask] = useState("");

  const [tasks, setTasks] = useState([]);

  const [message, setMessage] = useState("");

  const login = async () => {
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/api/v1/auth/login",
        {
          email,
          password,
        }
      );

      setToken(res.data.access_token);
      setMessage("Login successful ✅");
    } catch {
      setMessage("Login failed ❌");
    }
  };

  const createTask = async () => {
    try {
      await axios.post(
        "http://127.0.0.1:8000/api/v1/tasks/",
        {
          title: task,
          description: task,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setTask("");
      setMessage("Task created ✅");

      fetchTasks();
    } catch {
      setMessage("Task creation failed ❌");
    }
  };

  const fetchTasks = async () => {
    try {
      const res = await axios.get(
        "http://127.0.0.1:8000/api/v1/tasks/",
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setTasks(res.data);
    } catch {
      setMessage("Unable to load tasks ❌");
    }
  };

  return (
    <div className="container">

      <div className="card">

        <h1>Backend Assignment</h1>

        <p className="subtitle">
          Authentication + Role Based Access + CRUD
        </p>


        <div className="section">

          <h3>Login</h3>

          <input
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button onClick={login}>
            Login
          </button>

        </div>


        <div className="section">

          <h3>Tasks</h3>

          <input
            placeholder="Enter task"
            value={task}
            onChange={(e) => setTask(e.target.value)}
          />

          <div className="buttonRow">

            <button onClick={createTask}>
              Create Task
            </button>

            <button onClick={fetchTasks}>
              Load Tasks
            </button>

          </div>

        </div>


        {message && (
          <p className="message">
            {message}
          </p>
        )}


        <div className="taskList">

          {tasks.map((item) => (
            <div
              className="taskCard"
              key={item.id}
            >
              <h4>{item.title}</h4>

              <p>{item.description}</p>
            </div>
          ))}

        </div>

      </div>

    </div>
  );
}
import { useEffect, useState } from "react";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [username, setUsername] = useState("");
  const [form, setForm] = useState({ username: "", password: "" });

  const BACKEND = "http://localhost:5000"; // Replace with Render backend URL when deployed

  useEffect(() => {
    fetch(`${BACKEND}/api/check`, {
      credentials: "include",
    })
      .then(res => res.json())
      .then(data => {
        setLoggedIn(data.logged_in);
        setUsername(data.username || "");
      });
  }, []);

  const handleLogin = async () => {
    const res = await fetch(`${BACKEND}/api/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify(form),
    });

    const data = await res.json();
    if (data.success) {
      setLoggedIn(true);
      setUsername(form.username);
    } else {
      alert(data.message);
    }
  };

  const handleLogout = async () => {
    await fetch(`${BACKEND}/api/logout`, {
      method: "POST",
      credentials: "include",
    });
    setLoggedIn(false);
    setUsername("");
    setForm({ username: "", password: "" });
  };

  return (
    <div style={{ textAlign: "center", marginTop: "80px" }}>
      <h1>React + Flask Auth Demo</h1>
      {loggedIn ? (
        <>
          <p>Welcome, {username}!</p>
          <button onClick={handleLogout}>Logout</button>
          
        </>
      ) : (
        <div>
          <input
            type="text"
            placeholder="Username"
            value={form.username}
            onChange={(e) => setForm({ ...form, username: e.target.value })}
          />
          <input
            type="password"
            placeholder="Password"
            value={form.password}
            onChange={(e) => setForm({ ...form, password: e.target.value })}
          />
          <br />
          <button onClick={handleLogin}>Login</button>
        </div>
      )}
    </div>
  );
}

export default App;

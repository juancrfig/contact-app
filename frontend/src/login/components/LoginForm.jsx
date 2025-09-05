import { useState } from 'react';
import styles from './LoginForm.module.css';

function LoginForm() {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
    }

    const handleUsernameChange = (event) => {
        setUsername(event.target.value);
    };
    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    }

    return (
      <div className={styles.screen}>
        <form onSubmit={handleSubmit} className={styles.card} aria-labelledby="loginTitle">
          <h1 id="loginTitle" className={styles.title}>Welcome back</h1>
          <div className={styles.field}>
            <label className={styles.label} htmlFor="username">Username</label>
            <input
              className={styles.input}
              type="text"
              id="username"
              value={username}
              onChange={handleUsernameChange}
              placeholder="Enter your username"
              autoComplete="username"
            />
          </div>
          <div className={styles.field}>
            <label className={styles.label} htmlFor="password">Password</label>
            <input
              className={styles.input}
              type="password"
              id="password"
              value={password}
              onChange={handlePasswordChange}
              placeholder="••••••••"
              autoComplete="current-password"
            />
          </div>
          <div className={styles.actions}>
            <button className={styles.btnPrimary} type="submit">Login</button>
            <button className={styles.btnGhost} type="button">Register</button>
          </div>
        </form>
      </div>
    );
}

export default LoginForm;
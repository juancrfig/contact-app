import { useState } from 'react';

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
      <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="username" >Username </label>
            <input type="text" id="username" value={username} onChange={handleUsernameChange} />
          </div>
          <div>
              <label htmlFor="password">Password</label>
              <input type="password" id="password" value={password} onChange={handlePasswordChange} />/
          </div>
          <button type="submit">Login</button>
          <button type="button">Register</button>
      </form>
    );
}

export default LoginForm;
import './App.css';
import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          byroncooks
          <h1>Filipino Food</h1>
          <h3>for the homesick and hungry</h3>
        </header>
      </div>
    </Router>
  );
}

export default App;

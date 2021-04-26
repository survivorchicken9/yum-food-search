import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './containers/Home.js';
import SearchContainer from './containers/SearchContainer';

const App = () => {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route exact path="/search">
            <SearchContainer />
          </Route>
          <Route exact path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

export default App;

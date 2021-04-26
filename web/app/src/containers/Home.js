import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';

const Home = () => {
  const [clicked, setClicked] = useState(false);

  if (clicked) return <Redirect to="/search" />;

  return (
    <div className="header-button" onClick={() => setClicked(true)}>
      <h3 className="header-text">Filipino Food 🇵🇭</h3>
      <p className="header-text">
        <i>for the homesick and hungry</i>
      </p>
      <p id="byron">byroncooks</p>
    </div>
  );
};

export default Home;

import React, { useState } from 'react';
import Item from '../components/Item';

const SearchContainer = () => {
  const [input, setInput] = useState('');
  const [recipes, setRecipes] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();

    // make a fetch request w the input
  };

  return (
    <div id="search-container">
      <h1>Search for recipes</h1>
      <label for="ingredients">Ingredients that you have</label>
      <input
        type="text"
        id="ingredients"
        name="ingredients"
        placeholder="chicken, soy sauce, vinegar, peppercorn, bay leaf"
        onChange={(e) => setInput(e)}
      />
      <button className="btn submit-btn" onClick={(e) => handleSubmit(e)}>
        Search
      </button>
      <button className="btn clear-btn">Clear previous search</button>
      <div id="recipes">
        {recipes.map((recipe) => (
          <Item {...recipe} />
        ))}
      </div>
    </div>
  );
};

export default SearchContainer;

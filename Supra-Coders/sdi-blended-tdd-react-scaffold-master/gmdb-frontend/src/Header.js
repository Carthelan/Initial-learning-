import React, { useState }  from 'react'
import { Link } from 'react-router-dom'
import './Header.css'


function Header({ onSearch, gotoHome, userName, logout }) {
  const [movieSearch, setMovieSearch] = useState('');

  const handleMovieSearch = () => {
    onSearch(movieSearch)
  }

  const handleSearchChange = (event) => {
    setMovieSearch(event.target.value)
  }

  const handleGoToHome = () => {
    gotoHome();
  }

    return (
    <div className="movieHeader">
      <div className="homepage-pane">
        <Link to={"/"}>
            <ul className="homepage-button" onClick={handleGoToHome}>GMDB</ul>
        </Link>
        <p>Welcome: {userName}</p>
        <button onClick={logout}>Logout</button>
      </div>
      <div className="search-bar">
      <input
        type="text"
        placeholder="Search"
        value={movieSearch}
        onChange={handleSearchChange}
      />
      <button onClick={handleMovieSearch}>Search</button>
      </div>

    </div>
    )
}

export default Header;
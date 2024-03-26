import React, { useState, useEffect }  from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import MovieCard from "./movieCard.js"
import Header from "./Header.js"
import MovieDetails from './MovieDetails';
import "./App.css"

function App() {

  //make user.json with username & password
  //conditionally render below handleGoTohome to check if user is logged in
  //check input fields against user.json
  //if user + password in user.json pass through to render the webpage

  const [movieData, setMovieData] = useState([])
  const [clickedMovie, setClickedMovie] = useState(null)
  const [filteredMovies, setFilteredMovies] = useState([])
  const [logInStatus, setLogInStatus] = useState(false)
  const userInfo = [{"id": 1, "username": "fudpucker", "password": "password", "name": "Michael"},{"id": 2, "username": "Carthelan", "password": "password", "name": "Kristofer"}]
  const [userUsername, setUserUsername] = useState('');
  const [userPassword, setUserPassword] = useState('');

  useEffect(() => {
    fetch("http://localhost:3001/movies")
    .then(res => res.json())
    .then(data => {
      setMovieData(data);
      setFilteredMovies(data);
    })
    .catch(e => console.log(e))
  }, []);

  useEffect(() => {
    const loggedIn = localStorage.getItem('loggedIn');
    if (loggedIn === 'true') {
      setLogInStatus(true);
      setUserUsername(localStorage.getItem('username'));
    }
  }, []);

  const handleMovieClicked = (movieId) => {
    setClickedMovie(movieId);
    console.log(movieId)
  };

  const handleMovieSearch = (query) => {
    const filtered = movieData.filter(movie =>
      movie.title.toLowerCase().includes(query.toLowerCase())
      );
    setFilteredMovies(filtered);
  };

  const handleGoToHome  = () => {
    //setFilteredMovies(movieData);
    window.location.href = '/';
  };

  const handleLogOut = () => {
    localStorage.setItem('loggedIn', 'false');
    setLogInStatus(false);
    <link to={'/'}/>
  }

  const logIn = () => {
    const user = userInfo.find(user => user.username === userUsername && user.password === userPassword);
    if (user) {
      setLogInStatus(true);
      localStorage.setItem('loggedIn', 'true');
      localStorage.setItem('username', `${userUsername}`)
    } else {
      setLogInStatus(false);
    }
  }

  if (logInStatus === false) {
    return(
      <div>
        <h1>Please Log In</h1>
        <form>
          <input
            type='text'
            placeholder="Username"
            value={userUsername}
            onChange={e => setUserUsername(e.target.value)}
          />
          <input
            type='password'
            placeholder="password"
            value={userPassword}
            onChange={e => setUserPassword(e.target.value)}
          />
          <button onClick={logIn}>Log In</button>
        </form>
      </div>
    )
  }

  if (!movieData) {
    return(
      <h1>
        Still Loading
      </h1>
    )
  };

  return (
    <Router>
      <div>
        <Header onSearch={handleMovieSearch} gotoHome={handleGoToHome} userName={userUsername} logout={handleLogOut} />
        <Routes>
          <Route path="/" element={
            <div className="posterContainer">
              {filteredMovies.map((movie) => (
                <MovieCard
                  key={movie.movieId}
                  moviePoster={movie.poster}
                  movieId={movie.movieId}
                  movieTitle={movie.title}
                  movieClicked={() => handleMovieClicked(movie.movieId)}
                />
              ))}
            </div>
          } />
          <Route path="/movie/:id" element={<MovieDetails details={movieData.find(movie => movie.movieId === clickedMovie)} />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
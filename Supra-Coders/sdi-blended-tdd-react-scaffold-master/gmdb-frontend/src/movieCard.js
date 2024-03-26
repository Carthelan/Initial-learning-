import React from 'react';
import { Link } from 'react-router-dom';
import './movieCard.css';

function MovieCard({ moviePoster, movieId, movieTitle, movieClicked }) {
  return (
    <div className="moviePane" onClick={() => movieClicked(movieId)}>
      <Link to={`/movie/${movieId}`}>
        <img src={moviePoster} alt={movieTitle} />
      </Link>
    </div>
  );
}

export default MovieCard;
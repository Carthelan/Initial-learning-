import React from 'react';
import "./MovieDetails.css"

function MovieDetails({ details }) {
  if (!details) {
    return (
      <div>
        <h2>Loading...</h2>
      </div>
    );
  }

  return (
    <>
        <p> </p>
        <div className="moviePaneContainer">
          <div className="photoPane">
            <img src={details.poster} alt={details.title} />
          </div>
          <div className="detailsPane">
            <h1>{details.title}</h1>
            <h2><b>Released</b> {details.released}</h2>
            <p><b>Genre</b>: {details.genre}</p>
            <p><b>Actors</b>: {details.actors}</p>
            <p>{details.plot}</p>
          </div>
        </div>
    </>
  );
}

export default MovieDetails;
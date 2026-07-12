async function getRecommendations(mood) {

    const response = await fetch("/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            mood: mood
        })
    });

    const movies = await response.json();

    displayMovies(movies);
}


function displayMovies(movies) {

    const movieContainer = document.getElementById("movie-container");

    movieContainer.innerHTML = "";

    if (movies.length === 0) {
        movieContainer.innerHTML = "<h3>No movies found.</h3>";
        return;
    }

    movies.forEach(movie => {

        movieContainer.innerHTML += `
            <div class="movie-card">

                <img src="${movie.poster}" alt="${movie.title}">

                <h3>${movie.title}</h3>

                <p><strong>⭐ Rating:</strong> ${movie.rating}</p>

                <p><strong>📅 Release:</strong> ${movie.release_date}</p>

                <p>${movie.overview}</p>

            </div>
        `;

    });

}

async function searchMovie() {

    const movieName = document.getElementById("movie-search").value;

    if (movieName.trim() === "") {
        alert("Please enter a movie name.");
        return;
    }

    const response = await fetch("/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            movie: movieName
        })
    });

    const movies = await response.json();

    displayMovies(movies);
}
import requests
from config import TMDB_API_KEY

BASE_URL = "https://api.themoviedb.org/3"

# Mood → Genre Mapping
MOOD_GENRES = {
    "happy": 35,       # Comedy
    "sad": 18,         # Drama
    "romantic": 10749, # Romance
    "excited": 28,     # Action
    "relaxed": 99      # Documentary
}


def get_movie_details(mood):
    """
    Returns a list of movies based on the selected mood.
    """

    genre_id = MOOD_GENRES.get(mood.lower())

    if not genre_id:
        return []

    url = f"{BASE_URL}/discover/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "with_genres": genre_id,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "page": 1
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    data = response.json()

    movies = []

    for movie in data.get("results", [])[:10]:

        poster = movie.get("poster_path")

        if poster:
            poster = f"https://image.tmdb.org/t/p/w500{poster}"
        else:
            poster = ""

        movies.append({
            "title": movie.get("title"),
            "overview": movie.get("overview"),
            "poster": poster,
            "rating": movie.get("vote_average"),
            "release_date": movie.get("release_date")
        })

    return movies


def search_movie(movie_name):
    """
    Returns movies matching the search query.
    """

    url = f"{BASE_URL}/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_name,
        "language": "en-US"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    data = response.json()

    movies = []

    for movie in data.get("results", [])[:10]:

        poster = movie.get("poster_path")

        if poster:
            poster = f"https://image.tmdb.org/t/p/w500{poster}"
        else:
            poster = ""

        movies.append({
            "title": movie.get("title"),
            "overview": movie.get("overview"),
            "poster": poster,
            "rating": movie.get("vote_average"),
            "release_date": movie.get("release_date")
        })

    return movies
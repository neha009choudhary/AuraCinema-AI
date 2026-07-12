from flask import Flask, render_template, request, jsonify
from movies import get_movie_details, search_movie

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    mood = data.get("mood")

    movies = get_movie_details(mood)

    return jsonify(movies)


@app.route("/search", methods=["POST"])
def search():

    data = request.get_json()

    movie_name = data.get("movie")

    movies = search_movie(movie_name)

    return jsonify(movies)


if __name__ == "__main__":
    app.run(debug=True)
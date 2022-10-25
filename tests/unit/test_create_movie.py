# TODO: Feature 2
from src.repositories.movie_repository import MovieRepository
from src.models.movie import Movie

def test_create_movie():
    
    movie = MovieRepository()
    movie.create_movie('13 hours', 'Michael Bay', 5)
    assert len(movie.get_all_movies()) == 1
    movie.create_movie('Iron Man', 'JOn Favreau', 5)
    assert len(movie.get_all_movies()) == 2
    
def test_movie_model():
    movie = Movie('Thor: Love and Thunder', 'Taika Waititi', 3)

    assert type(movie) == Movie
    assert movie.title == 'Thor: Love and Thunder'
    assert movie.director == 'Taika Waititi'
    assert movie.rating == 3

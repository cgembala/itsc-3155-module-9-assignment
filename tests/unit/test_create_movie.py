# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repository = get_movie_repository()

def test_create_movie():
    
    
    movie_repository.create_movie('13 hours', 'Michael Bay', 5)
    assert len(movie_repository.get_all_movies()) == 1
    movie_repository.create_movie('Iron Man', 'JOn Favreau', 5)
    assert len(movie_repository.get_all_movies()) == 2
    
def test_movie_model():
    movie = Movie('Thor: Love and Thunder', 'Taika Waititi', 3)

    assert type(movie) == Movie
    assert movie.title == 'Thor: Love and Thunder'
    assert movie.director == 'Taika Waititi'
    assert movie.rating == 3

# # TODO: Feature 3
from turtle import title
from app import app, movie_repository, search_movies

def test_get_movie_by_title():
    movie2 = movie_repository.create_movie("Black Adam", "Jaume Collet-Serra", 7.5)
    movie3 = movie_repository.create_movie("Deadpool", "Ryan Reynolds", 8)
    test_app = app.test_client()
    response = test_app.get('/movies/search')
    
    if movie3 == title:
        assert b'<td>Deadpool</td>' in response.data
        assert b'<td>Ryan Reynolds</td>' in response.data
        assert b'<td>8</td>' in response.data
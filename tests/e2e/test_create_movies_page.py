# TODO: Feature 2
from flask.testing import FlaskClient


def test_create_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/new')
    response_data = response.data
    
    assert b'<h1 class="mb-5">Create Movie Rating</h1>' in response_data
    assert b'<p class="mb-3">Create a movie rating below</p>' in response_data
    assert b'<input type="text" id="name" name="name" autocomplete="off"><br>' in response_data
    assert b'<input type="text" id="director" name="director" autocomplete="off"><br>' in response_data
    assert b'<select id="rating" name="rating">' in response_data
    

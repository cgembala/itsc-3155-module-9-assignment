# TODO: Feature 1


from app import app, movie_repository





def test_get_movies():
    movie_repository.create_movie('Flash', 'Seth', 1)
    movie_repository.create_movie('Adam', 'Beth', 2)
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert b'<th> Movie </th>' in response.data
    assert b'<td> Flash </td>' in response.data
    assert b'<td> Seth </td>' in response.data
    assert b'<td> 1 </td>' in response.data
    assert b'<td> Adam </td>' in response.data
    assert b'<td> Beth </td>' in response.data
    assert b'<td> 2 </td>' in response.data
    assert b'<td> Batman </td>' not in response.data
    assert b'<td> Carry </td>' not in response.data
    assert b'<td> 3 </td>' not in response.data

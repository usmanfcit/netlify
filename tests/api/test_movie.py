import pytest

from .factories import MovieFactory


@pytest.mark.django_db
def test_movie_creation(staff_auth_client):
    movie = MovieFactory.build()
    movie_data = {
        "movie_name": movie.movie_name,
        "category": movie.category,
        "description": movie.description,
        "year_released": movie.year_released,
        "director": movie.director,
        "rating": movie.rating,
    }
    response = staff_auth_client.post("/api/netlify-movies/create/", movie_data, content_type="application/json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_movie_creation_fail_unauthenticated(db, client):
    movie = MovieFactory.build()
    movie_data = {
        "movie_name": movie.movie_name,
        "category": movie.category,
        "description": movie.description,
        "year_released": movie.year_released,
        "director": movie.director,
        "rating": movie.rating,
    }
    response = client.post("/api/netlify-movies/create/", movie_data, content_type="application/json")

    assert response.status_code == 401


@pytest.mark.django_db
def test_movie_listing(db, auth_client):
    MovieFactory.create_batch(3)
    client, _ = auth_client(email="test@gmail.com")
    response = client.get("/api/netlify-movies/")
    assert response.status_code == 200
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_movie_listing_empty(db, auth_client):
    client, _ = auth_client(email="test@gmail.com")
    response = client.get("/api/netlify-movies/")
    assert response.status_code == 404
    assert not isinstance(response.data, list)


@pytest.mark.django_db
def test_retrieve_movie(auth_client):
    client, _ = auth_client(email="test@gmail.com")
    movie = MovieFactory.create()
    response = client.get(f"/api/netlify-movies/get/{movie.id}")
    assert response.status_code == 200
    assert "movie_name" in response.data


@pytest.mark.django_db
def test_retrieve_movie_fail(client):
    movie = MovieFactory.create()

    response = client.get(f"/api/netlify-movies/get/{movie.id}")

    assert response.status_code == 401
    assert response.data["detail"] == "Authentication credentials were not provided."
    assert "movie_name" not in response.data
    assert "category" not in response.data
    assert "description" not in response.data


@pytest.mark.django_db
def test_delete_movie(staff_auth_client):
    movie = MovieFactory.create()
    response = staff_auth_client.delete(f"/api/netlify-movies/delete/{movie.id}")

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_movie_fail_unauthorized(auth_client):
    movie = MovieFactory.create()
    client, _ = auth_client(email="test@gmail.com")
    response = client.delete(f"/api/netlify-movies/delete/{movie.id}")    # Unauthorized

    assert response.status_code == 403


@pytest.mark.django_db
def test_delete_movie_fail_not_found(staff_auth_client):
    movie = MovieFactory.create()
    response = staff_auth_client.delete(f"/api/netlify-movies/delete/2")    # Not found

    assert response.status_code == 404


@pytest.mark.django_db
def test_update_movie(staff_auth_client):
    movie = MovieFactory.create()
    payload = dict(
        movie_name="Titanic-4",
        category="Mystery",
        description="Random",
        year_released="2001",
        director="El Pacino",
        rating=9.8
    )
    response = staff_auth_client.put(f"/api/netlify-movies/update/{movie.id}", data=payload,
                                     content_type="application/json")

    assert response.status_code == 200
    assert "movie_name" in response.data


@pytest.mark.django_db
def test_update_movie_fail(staff_auth_client):
    movie = MovieFactory.create()

    payload = dict(
        category="Mystery",
        description="Random",
        year_released="2001",
        director="El Pacino",
        rating=9.8
    )
    response = staff_auth_client.put(f"/api/netlify-movies/update/{movie.id}", data=payload,
                                     content_type="application/json")

    assert response.status_code == 400
import pytest


@pytest.mark.django_db
def test_movie_creation(db, auth_client):
    movie = {
        "movie_name": "Titanic-2",
        "category": "Adventure",
        "description": "Random",
        "year_released": "2001",
        "director": "El Pacino",
        "rating": 5.2
    }
    response = auth_client.post("/api/netlify-movies/create/", movie, content_type="application/json")

    assert response.status_code == 201


def test_movie_creation_fail_unauthenticated(db, client):
    movie = {
        "movie_name": "Titanic-2",
        "category": "Adventure",
        "description": "Random",
        "year_released": "2001",
        "director": "El Pacino",
        "rating": 5.2
    }
    response = client.post("/api/netlify-movies/create/", movie, content_type="application/json")

    assert response.status_code == 401


@pytest.mark.django_db
def test_movie_listing(db, client):
    response = client.get("/api/netlify-movies/")

    assert response.status_code == 200
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_retrieve_movie(auth_client, movie):
    response = auth_client.get("/api/netlify-movies/get/1")
    assert response.status_code == 200
    assert "movie_name" in response.data


@pytest.mark.django_db
def test_retrieve_movie_fail(client, movie):
    response = client.get("/api/netlify-movies/get/1")

    assert response.status_code == 401
    assert response.data["detail"] == "Authentication credentials were not provided."
    assert "movie_name" not in response.data
    assert "category" not in response.data
    assert "description" not in response.data

@pytest.mark.django_db
def test_delete_movie(auth_client, client, movie):

    response = auth_client.delete("/api/netlify-movies/delete/1")
    response_client = auth_client.delete("/api/netlify-movies/delete/3")    # Unauthorized

    assert response.status_code == 200
    assert response_client.status_code == 404


@pytest.mark.django_db
def test_delete_movie_fail(client, movie):

    response = client.delete("/api/netlify-movies/delete/1")    # Unauthorized
    assert response.status_code == 401


@pytest.mark.django_db
def test_update_movie(auth_client, movie):
    payload = dict(
            movie_name="Titanic-4",
            category="Mystery",
            description= "Random",
            year_released= "2001",
            director= "El Pacino",
            rating= 9.8
    )
    response = auth_client.put("/api/netlify-movies/update/1", data=payload, content_type="application/json")

    assert response.status_code == 200
    assert "movie_name" in response.data


@pytest.mark.django_db
def test_update_movie_fail(auth_client, movie):
    payload = dict(
            category="Mystery",
            description= "Random",
            year_released= "2001",
            director= "El Pacino",
            rating= 9.8
    )
    response = auth_client.put("/api/netlify-movies/update/1", data=payload, content_type="application/json")

    assert response.status_code == 400
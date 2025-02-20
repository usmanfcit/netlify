import pytest
from django.contrib.auth import get_user_model
User = get_user_model()
from netlify_movies.models import Netflix

@pytest.fixture
def movie(db):
    movie = Netflix.objects.create(
        id = 1,
        movie_name= "Titanic-2",
        category= "Adventure",
        description= "Random",
        year_released= "2001",
        director= "El Pacino",
        rating= 5.2)
    return movie

@pytest.fixture
def staff_user(db):
    user = User.objects.create(
        id=1,
        email="staff@email.com",
        is_staff=True
    )
    user.set_password("staff1234")
    user.save()
    return user


@pytest.fixture
def auth_client(client, staff_user):
    """Fixture to authenticate user and return client with JWT token"""
    login_response = client.post(
        "/api/users/login/",
        {"email": staff_user.email, "password": "staff1234"},
        content_type="application/json"
    )

    assert login_response.status_code == 200

    # Extract token from response
    token = login_response.data["access"]
    client.defaults["HTTP_AUTHORIZATION"] = f"Bearer {token}"
    return client
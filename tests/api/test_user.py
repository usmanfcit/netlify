import pytest


@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
        email="usmantest@gmail.com",
        password="12345678",
        first_name="Usman",
        last_name="Test",
    )
    response = client.post("/api/users/register/", data=payload, content_type="application/json")

    data = response.data
    assert response.status_code == 201
    assert data["email"] == payload["email"]


def test_register_user_fail(client):
    payload = dict(
        first_name="Usman",
        last_name="Test",
    )
    response = client.post("/api/users/register/", data=payload, content_type="application/json")
    assert response.status_code == 400

    assert "email" in response.data
    assert response.data["email"][0] == "This field is required."
    assert response.data["password"][0] == "This field is required."


@pytest.mark.django_db
def test_login_user(client):
    payload = dict(
        email="usmantest@gmail.com",
        password="12345678",
        first_name="Usman",
        last_name="Test",
    )

    client.post("/api/users/register/", data=payload, content_type="application/json")
    response = client.post("/api/users/login/", dict(email="usmantest@gmail.com", password="12345678"),
                           content_type="application/json")

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_login_fail(client):
    response = client.post("/api/users/login/", dict(email="email@email.com", password=1234),
                           content_type="application/json")

    assert response.status_code == 401


@pytest.mark.django_db
def test_list_users(staff_auth_client):
    response = staff_auth_client.get("/api/users/")

    assert response.status_code == 200
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_list_users_fail(client):
    response = client.get("/api/users/")

    assert response.status_code == 401
    assert not isinstance(response.data, list)


@pytest.mark.django_db
def test_retrieve_user_own_profile(auth_client):
    client, user = auth_client(email="test@gmail.com")
    response = client.get(f"/api/users/{user.id}/")

    assert response.status_code == 200
    assert response.data["email"] == user.email


@pytest.mark.django_db
def test_retrieve_other_profile(auth_client):
    client1, user1 = auth_client(email="user1@test.com")
    client2, user2 = auth_client(email="user2@test.com")

    response = client2.get(f"/api/users/{user1.id}/")
    assert response.status_code == 403


@pytest.mark.django_db
def test_retrieve_user_unauthenticated(client):
    response = client.get("/api/users/1/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_retrieve_user_not_found(auth_client):
    client, user = auth_client(email="user1@test.com")
    response = client.get("/api/users/2/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_own_profile(auth_client):
    client, user = auth_client(email="user1@test.com")
    response = client.delete(f"/api/users/{user.id}/")
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_other_profile(auth_client):
    client1, user1 = auth_client(email="user1@test.com")
    client2, user2 = auth_client(email="user2@test.com")
    response = client2.delete(f"/api/users/{user1.id}/")
    assert response.status_code == 403


@pytest.mark.django_db
def test_update_own_profile(auth_client):
    client, user = auth_client(email="user1@test.com")
    payload = {
        "email": "user1_updated@test.com",
        "first_name": "Updated",
        "last_name": "User"
    }
    response = client.put(f"/api/users/{user.id}/", data=payload, content_type="application/json")
    assert response.status_code == 200
    assert response.data["email"] == "user1_updated@test.com"


@pytest.mark.django_db
def test_update_other_profile(auth_client):
    client1, user1 = auth_client(email="user1@test.com")
    client2, user2 = auth_client(email="user2@test.com")
    payload = {
        "email": "hacker@test.com",
        "first_name": "Hacker",
        "last_name": "User"
    }
    response = client2.put(f"/api/users/{user1.id}/", data=payload, content_type="application/json")
    assert response.status_code == 403


@pytest.mark.django_db
def test_update_user_fail_unauthorized(client):
    payload = dict(
        email="usmantestNEW@gmail.com",
        password="12345678",
        first_name="NEWUSMAN",
        last_name="Test",
    )
    response = client.put("/api/users/1/", data=payload, content_type="application/json")

    assert response.status_code == 401
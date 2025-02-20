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
    # ✅ 1. Assert status code 400
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
def test_list_users(auth_client):
    response = auth_client.get("/api/users/")

    assert response.status_code == 200
    assert isinstance(response.data, list)

@pytest.mark.django_db
def test_list_users_fail(client):
    response = client.get("/api/users/")

    assert response.status_code == 401
    assert not isinstance(response.data, list)


@pytest.mark.django_db
def test_retrieve_user(auth_client):
    response = auth_client.get("/api/users/1/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_retrieve_user_unauthenticated(client):
    response = client.get("/api/users/1/")
    assert response.status_code == 401

@pytest.mark.django_db
def test_retrieve_user_not_found(auth_client):
    response = auth_client.get("/api/users/-1/")
    assert response.status_code == 404

@pytest.mark.django_db
def test_delete_user(auth_client, client):

    response = auth_client.delete("/api/users/1/")
    response_client = client.delete("/api/users/1/")    # Unauthorized

    assert response.status_code == 204
    assert response_client.status_code == 401


@pytest.mark.django_db
def test_update_user(auth_client, client):
    payload = dict(
        email="usmantestNEW@gmail.com",
        password="12345678",
        first_name="NEWUSMAN",
        last_name="Test",
    )
    response = auth_client.put("/api/users/1/", data=payload, content_type="application/json")
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_user_fail(auth_client, client):
    payload = dict(
        email="usmantestNEW@gmail.com",
        password="12345678",
        first_name="NEWUSMAN",
        last_name="Test",
    )
    response = auth_client.put("/api/users/8/", data=payload, content_type="application/json")
    assert response.status_code == 404
    assert "email" not in response
    assert "password" not in response


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


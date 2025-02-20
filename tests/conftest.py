import pytest
from django.contrib.auth import get_user_model
User = get_user_model()


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
def staff_auth_client(client, staff_user):
    login_response = client.post(
        "/api/users/login/",
        {"email": staff_user.email, "password": "staff1234"},
        content_type="application/json"
    )

    assert login_response.status_code == 200
    token = login_response.data["access"]
    client.defaults["HTTP_AUTHORIZATION"] = f"Bearer {token}"
    return client


@pytest.fixture
def auth_client(db, client):
    def _auth_client(email, password="testpassword"):
        user = User.objects.create_user(email=email, password=password)
        user.save()
        test_client = client
        login_response = test_client.post(
            "/api/users/login/",
            {"email": email, "password": password},
            content_type="application/json"
        )

        assert login_response.status_code == 200, "Login failed for user"
        token = login_response.data["access"]
        test_client.defaults["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        return test_client, user

    return _auth_client
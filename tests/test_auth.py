import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_register_get_renders_form(client):
    response = client.get(reverse("accounts:register"))
    assert response.status_code == 200
    assert b"Register" in response.content


@pytest.mark.django_db
def test_register_post_creates_user_and_logs_in(client):
    response = client.post(
        reverse("accounts:register"),
        {"username": "newuser", "password1": "SecurePass123!", "password2": "SecurePass123!"},
    )
    assert response.status_code == 302
    assert response.url == reverse("chat:lobby")
    assert User.objects.filter(username="newuser").exists()
    assert client.session.get("_auth_user_id") is not None


@pytest.mark.django_db
def test_register_duplicate_username_shows_error(client):
    User.objects.create_user(username="taken", password="SecurePass123!")
    response = client.post(
        reverse("accounts:register"),
        {"username": "taken", "password1": "SecurePass123!", "password2": "SecurePass123!"},
    )
    assert response.status_code == 200
    assert b"already exists" in response.content.lower() or b"taken" in response.content.lower()


@pytest.mark.django_db
def test_register_weak_password_shows_error(client):
    response = client.post(
        reverse("accounts:register"),
        {"username": "weakuser", "password1": "123", "password2": "123"},
    )
    assert response.status_code == 200
    assert User.objects.filter(username="weakuser").exists() is False


@pytest.mark.django_db
def test_login_post_valid_credentials(client):
    User.objects.create_user(username="loginuser", password="SecurePass123!")
    response = client.post(
        reverse("accounts:login"),
        {"username": "loginuser", "password": "SecurePass123!"},
    )
    assert response.status_code == 302
    assert response.url == reverse("chat:lobby")
    assert client.session.get("_auth_user_id") is not None


@pytest.mark.django_db
def test_login_post_invalid_credentials(client):
    User.objects.create_user(username="loginuser", password="SecurePass123!")
    response = client.post(
        reverse("accounts:login"),
        {"username": "loginuser", "password": "wrongpassword"},
    )
    assert response.status_code == 200
    assert client.session.get("_auth_user_id") is None


@pytest.mark.django_db
def test_logout_clears_session(client):
    user = User.objects.create_user(username="logoutuser", password="SecurePass123!")
    client.force_login(user)
    assert client.session.get("_auth_user_id") is not None

    response = client.get(reverse("accounts:logout"))
    assert response.status_code == 302
    assert response.url == reverse("accounts:login")
    assert client.session.get("_auth_user_id") is None


@pytest.mark.django_db
def test_authenticated_user_redirected_from_register_login(client):
    user = User.objects.create_user(username="existing", password="SecurePass123!")
    client.force_login(user)

    register_response = client.get(reverse("accounts:register"))
    assert register_response.status_code == 302
    assert register_response.url == reverse("chat:lobby")

    login_response = client.get(reverse("accounts:login"))
    assert login_response.status_code == 302
    assert login_response.url == reverse("chat:lobby")

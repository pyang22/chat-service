import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_lobby_requires_login(client):
    response = client.get(reverse("chat:lobby"))
    assert response.status_code == 302
    assert reverse("accounts:login") in response.url


@pytest.mark.django_db
def test_lobby_shows_username_when_authenticated(client):
    user = User.objects.create_user(username="lobbyuser", password="SecurePass123!")
    client.force_login(user)

    response = client.get(reverse("chat:lobby"))
    assert response.status_code == 200
    assert b"Lobby" in response.content
    assert b"lobbyuser" in response.content


@pytest.mark.django_db
def test_lobby_no_500(client):
    user = User.objects.create_user(username="stableuser", password="SecurePass123!")
    client.force_login(user)

    response = client.get(reverse("chat:lobby"))
    assert response.status_code == 200

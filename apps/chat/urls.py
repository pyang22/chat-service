from django.urls import path

from apps.chat import views

app_name = "chat"

urlpatterns = [
    path("", views.lobby_view, name="lobby"),
]

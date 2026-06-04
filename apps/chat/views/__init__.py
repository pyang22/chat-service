from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def lobby_view(request):
    return render(request, "chat/lobby.html")

from django.shortcuts import render, get_object_or_404

from .models import *


def home_view(request):
    return render(request, 'index.html')


def clubs_view(request):
    clubs = Club.objects.all()

    country_query = request.GET.get('country')
    if country_query:
        clubs = clubs.filter(country__id=country_query)

    context = {
        'clubs': clubs
    }
    return render(request, 'clubs.html', context)


def players_view(request):
    players = Player.objects.order_by('-price')
    context = {
        'players': players
    }
    return render(request, 'players.html', context)


def club_retrieve_view(request, pk):
    club = get_object_or_404(Club, pk=pk)
    players = Player.objects.filter(club=club).order_by('-price')
    context = {
        'club': club,
        'players': players
    }
    return render(request, 'club-info.html', context)


def tryouts_view(request):
    return render(request, 'tryouts.html')

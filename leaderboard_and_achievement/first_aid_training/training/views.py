# Create your views here.
from django.shortcuts import render

def leaderboard(request):
    return render(request, 'leaderboard.html')

def achievements(request):
    return render(request, 'achievements.html')
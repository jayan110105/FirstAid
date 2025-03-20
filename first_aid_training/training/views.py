from django.shortcuts import render

def modules(request):
    return render(request, 'modules.html')

def scenarios(request):
    return render(request, 'scenarios.html')

def achievements(request):
    return render(request, 'achievements.html')

def leaderboard(request):
    return render(request, 'leaderboard.html')

def profile(request):
    return render(request, 'profile.html')

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def leaderboard(request):
    return render(request, 'leaderboard/leaderboard.html', {})

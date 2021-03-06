from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from contest.models import Contest
from userprof.models import UserProfile


def home_view(request):
    all_contests = Contest.objects.all()
    return render(request, 'home/home_view.html', {'all_contests': all_contests, })

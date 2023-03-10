from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Opinion
from .forms import OpinionForm
# Create your views here.


def all_opinions(request):
    opinions = Opinion.objects.all()
    return render(request, 'all_opinions.html', {'opinions': opinions})


def single_opinion(request):
    opinion = Opinion.objects.first()

    return render(request, 'opinion.html', {'opinion': opinion})


@login_required
def add_opinion(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST, user=request.user, time=datetime.now())
        if form.is_valid():
            form.save()
            return redirect('all_opinions')
    else:
        form = OpinionForm()
    context = {'form': form}
    return render(request, 'add_opinion.html', context)

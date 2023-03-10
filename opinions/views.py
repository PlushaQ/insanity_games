from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Opinion
from .forms import OpinionForm
# Create your views here.


def all_opinions(request):
    opinions = Opinion.objects.order_by("-time")
    return render(request, 'all_opinions.html', {'opinions': opinions})


def single_opinion(request, opinion_id):
    opinion = get_object_or_404(Opinion, pk=opinion_id)

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


@login_required
def delete_opinion(request, opinion_id):
    opinion = get_object_or_404(Opinion, pk=opinion_id)

    # Only allow the user who added the opinion to delete it
    if opinion.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this opinion.")

    opinion.delete()
    return redirect('all_opinions')

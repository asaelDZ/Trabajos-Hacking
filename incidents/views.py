from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Incident
from .forms import IncidentForm

from accounts.models import UserProfile


@login_required
def home(request):

    incidents = Incident.objects.all()

    return render(request, 'incidents/home.html', {
        'incidents': incidents
    })


@login_required
def create(request):

    form = IncidentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        incident = form.save(commit=False)

        incident.reported_by = request.user

        incident.save()

        return redirect('incidents:home')

    return render(request, 'incidents/create.html', {
        'form': form
    })


@login_required
def detail(request, pk):

    incident = get_object_or_404(Incident, pk=pk)

    return render(request, 'incidents/detail.html', {
        'incident': incident
    })


@login_required
def update(request, pk):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'analyst'}
    )

    if not profile.is_admin():

        return HttpResponseForbidden(
            'Only admins can edit incidents.'
        )

    incident = get_object_or_404(Incident, pk=pk)

    form = IncidentForm(
        request.POST or None,
        instance=incident
    )

    if request.method == 'POST' and form.is_valid():

        form.save()

        return redirect('incidents:home')

    return render(request, 'incidents/update.html', {
        'form': form
    })


@login_required
def delete(request, pk):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'analyst'}
    )

    if not profile.is_admin():

        return HttpResponseForbidden(
            'Only admins can delete incidents.'
        )

    incident = get_object_or_404(Incident, pk=pk)

    if request.method == 'POST':

        incident.delete()

        return redirect('incidents:home')

    return render(request, 'incidents/confirm_delete.html', {
        'incident': incident
    })
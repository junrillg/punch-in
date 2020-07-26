from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from meetings.forms import MeetingForm
from meetings.models import Meeting


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()

    return render(request, "meetings/new.html", {"form": form})

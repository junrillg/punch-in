from django.urls import path, include

from authentication.views import login

from dashboard.views import index

urlpatterns = [
    path("login", login),
    path("", index),
    path("meetings/", include("meetings.urls")),
]

from django.urls import path

from meetings.views import detail, new

urlpatterns = [
    path("<int:id>", detail, name="detail"),
    path("new", new, name="new"),
]

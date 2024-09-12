from django.urls import path
from django.views.generic import RedirectView

from .views import ClientArchiveView
from .views import ClientCreateView
from .views import ClientDetailView
from .views import ClientListView
from .views import ClientUpdateView
from .views import CoachingSessionCreateView
from .views import index

app_name = "coach"
urlpatterns = [
    path("", index, name="dashboard"),
    path("client/list", ClientListView.as_view(), name="client_list"),
    path("client/detail/<int:pk>", ClientDetailView.as_view(), name="client_detail"),
    path("client/create/", ClientCreateView.as_view(), name="client_create"),
    path("client/<int:pk>/update", ClientUpdateView.as_view(), name="client_update"),
    path("client/<int:pk>/archive", ClientArchiveView.as_view(), name="client_archive"),
    path(
        "coachingsession/<int:client_id>/create",
        CoachingSessionCreateView.as_view(),
        name="coachingsession_create",
    ),
    path(
        "favicon.svg",
        RedirectView.as_view(url="/static/images/favicons/favicon.ico"),
    ),
]

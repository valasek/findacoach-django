from django.urls import path

from .views import ClientArchiveView
from .views import ClientCreateView
from .views import ClientDetailView
from .views import ClientListView
from .views import ClientUpdateView
from .views import index

app_name = "coach"
urlpatterns = [
    path("", index, name="dashboard"),
    path("client/list", ClientListView.as_view(), name="client_list"),
    path("client/detail/<int:pk>", ClientDetailView.as_view(), name="client_detail"),
    path("client/create", ClientCreateView.as_view(), name="client_create"),
    path("client/update/<int:pk>", ClientUpdateView.as_view(), name="client_update"),
    path("client/archive/<int:pk>", ClientArchiveView.as_view(), name="client_archive"),
]

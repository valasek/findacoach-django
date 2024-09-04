from typing import Any

from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .models import Client
from .models import CoachingSession
from .models import Profile


def index(request):
    user = request.user
    upcomming_sessions = CoachingSession.upcomming_sessions(user, 7)
    total_coached_hours = Profile.total_coached_hours(user)

    context = {
        "coach": user.name,
        "total_coached_hours": total_coached_hours,
        "upcomming_sessions": upcomming_sessions,
    }
    return render(request, "dashboard.html", context)


class ClientListView(ListView):
    model = Client
    template_name = "client/list.html"


class ClientDetailView(DetailView):
    model = Client
    template_name = "client/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["client"] = kwargs["object"].client
        return context


class ClientCreateView(CreateView):
    model = Client
    template_name = "client/create.html"


class ClientUpdateView(UpdateView):
    model = Client
    template_name = "client/update.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["client"] = kwargs["object"].client
        return context


class ClientArchiveView(UpdateView):
    model = Client
    template_name = "client/archive.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["client"] = kwargs["object"].client
        return context

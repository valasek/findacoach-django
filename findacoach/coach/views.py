from typing import Any

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .forms import ClientForm
from .forms import CoachingSessionForm
from .models import Client
from .models import CoachingSession
from .models import Profile


@login_required
def index(request):
    user = request.user
    upcomming_sessions = CoachingSession.upcomming_sessions(user, 7)
    total_coached_hours = Profile.total_coached_hours(user)
    active_clients_count = Client.clients_count(user, archived=False)
    archived_clients_count = Client.clients_count(user, archived=True)

    context = {
        "coach": user.name,
        "total_coached_hours": total_coached_hours,
        "upcomming_sessions": upcomming_sessions,
        "active_clients_count": active_clients_count,
        "archived_clients_count": archived_clients_count,
    }
    return render(request, "dashboard.html", context)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "client/list.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Client.objects.filter(archived=False, coach=self.request.user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "client/detail.html"


class ClientCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = "client/client_form.html"
    success_message = "Client sucessfully saved"
    success_url = reverse_lazy("coach:dashboard")

    def form_valid(self, form):
        form.instance.coach = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "client/client_form.html"
    success_message = "Client sucessfully updated"
    success_url = reverse_lazy("coach:dashboard")

    def form_valid(self, form):
        form.instance.coach = self.request.user
        return super().form_valid(form)


class ClientArchiveView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Client
    fields = []  # No fields in the form
    success_message = "Client sucessfully archived"
    success_url = reverse_lazy("coach:client_list")

    def get(self, request, *args, **kwargs):
        # Skip the confirmation page and directly update the object
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.archived = True
        self.object.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.get_success_url())


class CoachingSessionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CoachingSession
    form_class = CoachingSessionForm
    template_name = "coachingsession/create.html"
    success_message = "Coaching session sucessfully saved"
    success_url = reverse_lazy("coach:dashboard")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if "client_id" in self.kwargs:
            kwargs["initial"] = {"client": self.kwargs["client_id"]}
        return kwargs


class CoachingSessionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CoachingSession
    form_class = CoachingSessionForm
    template_name = "coachingsession/session_form.html"
    success_message = "Session sucessfully updated"
    success_url = reverse_lazy("coach:dashboard")

    def form_valid(self, form):
        form.instance.coach = self.request.user
        return super().form_valid(form)

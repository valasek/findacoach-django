from django.contrib import admin

from .models import Client
from .models import Coach
from .models import CoachingSession

admin.site.register(Coach)
admin.site.register(Client)
admin.site.register(CoachingSession)

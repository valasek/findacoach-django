from django.contrib import admin

from .models import Client
from .models import CoachingSession
from .models import Profile

admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(CoachingSession)

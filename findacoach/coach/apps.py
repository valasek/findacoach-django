from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoachConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "findacoach.coach"
    verbose_name = _("Coach")

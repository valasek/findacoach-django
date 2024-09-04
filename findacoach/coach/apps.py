from django.apps import AppConfig


class CoachConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "findacoach.coach"
    verbose_name = "Coach"

    def ready(self):
        import findacoach.coach.signals  # noqa: F401

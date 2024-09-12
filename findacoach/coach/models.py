# Create your models here.
"""DB models"""

from django.conf import settings
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Count
from django.db.models import Sum
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class TimeStampedModel(models.Model):
    """Timestamp abstract base class model"""

    created = models.DateTimeField(auto_now_add=True, verbose_name="Datum vytvoření")
    modified = models.DateTimeField(auto_now=True, verbose_name="Datum aktualizace")

    class Meta:
        """Meta class"""

        abstract = True


class Profile(TimeStampedModel):
    """Coach model, coach is a user as well"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="coach_user",
        verbose_name="User",
    )
    is_coach = models.BooleanField(default=True)
    # odmentorovanych hodnín - property

    class Meta:
        """Meta class"""

        verbose_name_plural = "profiles"
        # ordering = ["name"]  # noqa: ERA001

    def __str__(self):
        return f"{self.user.email}, {self.is_coach}"

    @classmethod
    def total_coached_hours(cls, coach):
        return Client.objects.filter(coach_id=coach).aggregate(
            total_hours=Sum("hours_delivered"),
        )["total_hours"]


class Client(TimeStampedModel):
    """Client model"""

    coach = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Coach",
    )
    name = models.CharField("Full Name", max_length=254, blank=False)
    email = models.EmailField(
        "Email address",
        unique=True,
        blank=False,
        null=False,
        max_length=254,
    )
    phone = PhoneNumberField("Phone number", unique=True, blank=True)
    company = models.CharField("Company", max_length=100, blank=True)
    position = models.CharField("Position", max_length=100, blank=True)
    hours_ordered = models.DecimalField(
        "Hours ordered",
        max_digits=5,
        decimal_places=1,
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(999.5)],
        help_text="Hours in 0.5 steps",
    )
    hours_delivered = models.DecimalField(
        "Hours delivered",
        max_digits=5,
        decimal_places=1,
        blank=True,
        null=True,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(999.5)],
        help_text="Hours in 0.5 steps",
    )
    coaching_goal = models.TextField(
        "Coaching goal",
        blank=True,
        help_text="Client goal as per ICF definition",
    )
    archived = models.BooleanField(default=False, blank=False)

    class Meta:
        """Meta class"""

        verbose_name_plural = "clients"
        ordering = ["name"]

    def __str__(self):
        return self.name

    @classmethod
    def clients_count(cls, coach, archived):
        return Client.objects.filter(coach_id=coach, archived=archived).aggregate(
            clients=Count("name"),
        )["clients"]


def current_time():
    return timezone.now().time()


class CoachingSession(TimeStampedModel):
    """Coaching session model"""

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
    date = models.DateField("Date", default=timezone.now)
    time = models.TimeField("Time", default=current_time)
    duration = models.DecimalField(
        "Duration",
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.5), MaxValueValidator(12)],
        help_text="Duration in hours",
    )
    note = models.TextField("Note", blank=True)
    homework = models.TextField("Homework", blank=True)
    realized = models.BooleanField("Realized", default=False)

    class Meta:
        """Meta class"""

        verbose_name_plural = "coaching sessions"
        # ordering = ["name"]  # noqa: ERA001
        # indexes = [models.Index(fields=["email"])]  # noqa: ERA001

    def __str__(self):
        return f"{self.date}, {self.time}, {self.duration}, {self.realized}"

    @classmethod
    def upcomming_sessions(cls, coach, session_count):
        """Returns upcomming session_count sessions per coach for all clients"""
        coaching_sessions = CoachingSession.objects.filter(
            client__coach=coach,
            realized=False,
        ).order_by("date", "time")[:session_count]
        upcomming_sessions = []
        for coaching_session in coaching_sessions:
            item = {
                "client_id": coaching_session.client.id,
                "name": coaching_session.client.name,
                "email": coaching_session.client.email,
                "phone": coaching_session.client.phone,
                "coaching_goal": coaching_session.client.coaching_goal,
                "hours_delivered": coaching_session.client.hours_delivered,
                "hours_ordered": coaching_session.client.hours_ordered,
                "session_id": coaching_session.id,
                "date": coaching_session.date,
                "time": coaching_session.time,
                "duration": coaching_session.duration,
                "homework": coaching_session.homework,
                "note": coaching_session.note,
            }
            upcomming_sessions.append(item)

        return upcomming_sessions

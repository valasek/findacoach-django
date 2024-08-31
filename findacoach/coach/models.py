# Create your models here.
"""DB models"""

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class TimeStampedModel(models.Model):
    """Timestamp abstract base class model"""

    created = models.DateTimeField(auto_now_add=True, verbose_name="Datum vytvoření")
    modified = models.DateTimeField(auto_now=True, verbose_name="Datum aktualizace")

    class Meta:
        """Meta class"""

        abstract = True


class Coach(TimeStampedModel):
    """Coach model, coach is a user as well"""

    name = models.CharField("Full Name", max_length=254, blank=True)
    # odmentorovanych hodnín - property

    class Meta:
        """Meta class"""

        verbose_name_plural = "choaches"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Client(TimeStampedModel):
    """Client model"""

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
        validators=[MinValueValidator(0), MaxValueValidator(999.5)],
        help_text="Hours in 0.5 steps",
    )
    hours_delivered = models.DecimalField(
        "Hours delivered",
        max_digits=5,
        decimal_places=1,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(999.5)],
        help_text="Hours in 0.5 steps",
    )
    coaching_goal = models.TextField(
        "Coaching goal",
        blank=True,
        help_text="Client goal as per ICF definition",
    )
    next_session_datetime = models.DateTimeField(
        "Next session date and time",
        null=True,
        blank=True,
    )

    class Meta:
        """Meta class"""

        verbose_name_plural = "clients"
        ordering = ["name"]

    def __str__(self):
        return self.name


class CoachingSession(TimeStampedModel):
    """Coaching session model"""

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="session_client",
        verbose_name="Client",
    )
    coach = models.ForeignKey(
        Coach,
        on_delete=models.CASCADE,
        related_name="session_coach",
        verbose_name="Coach",
    )
    datetime = models.DateTimeField("Date and time")
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
        return f"{self.coach}, {self.client}, {self.datetime}"

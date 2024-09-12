from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column
from crispy_forms.layout import Layout
from crispy_forms.layout import Row
from django import forms

from .models import Client
from .models import CoachingSession


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "name",
            "email",
            "phone",
            "company",
            "position",
            "hours_ordered",
            "hours_delivered",
            "coaching_goal",
            "archived",
        ]
        widgets = {
            "email": forms.EmailInput(),
            "phone": forms.TextInput(attrs={"type": "tel"}),
            "hours_ordered": forms.NumberInput(
                attrs={"step": 0.5, "min": 0, "max": 40},
            ),
            "hours_delivered": forms.NumberInput(
                attrs={"step": 0.5, "min": 0, "max": 40},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-2"),
                Column("email", css_class="col-md-2"),
                Column("phone", css_class="col-md-2"),
                Column("company", css_class="col-md-3"),
                Column("position", css_class="col-md-3"),
            ),
            Row(
                Column("coaching_goal", css_class="col-md-12"),
            ),
            Row(
                Column("hours_ordered", css_class="col-md-2"),
                Column("hours_delivered", css_class="col-md-2"),
                Column("archived", css_class="col-md-2"),
            ),
        )


class CoachingSessionForm(forms.ModelForm):
    class Meta:
        model = CoachingSession
        fields = ["client", "date", "time", "duration", "note", "homework", "realized"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "duration": forms.NumberInput(
                attrs={"step": 0.5, "min": 0, "max": 12, "value": 1},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column("client", css_class="col-md-2"),
                Column("date", css_class="col-md-2"),
                Column("time", css_class="col-md-2"),
                Column("duration", css_class="col-md-2"),
                Column("realized", css_class="col-md-2"),
            ),
            Row(
                Column("note", css_class="col-md-6"),
                Column("homework", css_class="col-md-6"),
            ),
        )

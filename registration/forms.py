from django.forms import forms, ModelForm

from . import models

class incidentform(ModelForm):
    class Meta:
        models=models.incident


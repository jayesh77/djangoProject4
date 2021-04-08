from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class incident(models.Model):
    Operations_Department = 'OD'
    Management_Department = 'MD'
    Accounts_Department = 'Ad'

    location_CHOICES = [
        (Operations_Department, 'Operations Department'),
        (Management_Department, 'Management Department'),
        (Accounts_Department, 'Accounts Department'),

    ]
    location = models.CharField(
        max_length=2,
        choices=location_CHOICES,
        default=Accounts_Department,
    )
    incident_department=models.TextField(max_length=200)

    Suspected_Cause=models.TextField(max_length=200)
    Initial_Severity_CHOICES = [
        ('Mild', 'Mild'),
        ('Moderate', 'Moderate'),
        ('Fatal', 'Fatal'),

    ]
    Initial_Severity = models.CharField(
        max_length=10,
        choices=Initial_Severity_CHOICES,
        default='Mild')
    environment_incident=models.BooleanField()
    Vehicle=models.BooleanField()
    property_damage=models.BooleanField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)


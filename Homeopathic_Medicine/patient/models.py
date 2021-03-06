from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone
from datetime import datetime, timedelta


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone_num = models.IntegerField()
    Gender = models.CharField(max_length=50,default='Male')
    email = models.EmailField(blank=True, default='NA')
    symptoms = models.CharField(max_length=100)
    medicine = models.CharField(max_length=100)
    created_at =models.DateTimeField(default=timezone.now())
    user = models.ManyToManyField(User)


# Create your models here.
class PatientAppointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone_num = models.IntegerField()
    Gender = models.CharField(max_length=50,default='Male')
    email = models.EmailField(blank=True, default='NA')
    user = models.ManyToManyField(User)
    Datetime = models.DateTimeField(default=timezone.now())


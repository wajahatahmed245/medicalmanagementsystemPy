from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#jnjni


class Appointments(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150, blank=True, default='Not Mentioned')
    phone_num = models.IntegerField()
    Gender = models.CharField(max_length=50, default='Male')
    email = models.EmailField(blank=True, default='Not Mentioned')
    Msg = models.TextField(blank=True, default='Not Mentioned')

    def __str__(self):
        return self.user.username
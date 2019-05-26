from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from patient.models import Patient
import django.utils.timezone as timezone



class MyUser(AbstractBaseUser):
    is_active = models.BooleanField(
        default=False
    )


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{} and time = {}".format(self.question_text, self.pub_date)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Visit(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptoms = models.TextField(null=False, blank=True, default="NA")
    symptomsMedicine = models.TextField(null=False, blank=False, default="NA")
    extraMediceine = models.TextField(blank=True, default="Not Recomended")
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return ('{} {}').format(self.patient.first_name, self.patient.last_name)


class Doctor_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clinic = models.CharField(max_length=50, null=False, blank=False, default="NA")
    gender = models.CharField(null=False, max_length=10, blank=False, default="NA")

    def __str__(self):
        return self.user.username

    # user bantay sath he yeh signal banay ga


@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Doctor_User.objects.create(user=instance)
    else:
        instance.doctor_user.save()

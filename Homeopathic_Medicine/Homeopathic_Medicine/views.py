from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404
from django.db import IntegrityError
from Doctor.models import Doctor_User as DP
import request


def sign_up(request):
    # Create user and save to the database
    context = {

    }
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        clinicname = request.POST.get('clinicname')
        pswd = request.POST.get('pswd')
        username = request.POST.get('username')
        sellist1 = request.POST.get('sellist1')
        print(sellist1)
        try:
            user = User.objects.create_user(username, email, pswd)

            username = request.user.username
            print(username)
            # Update fields and then save aga'bool' object is not callablein
            user.first_name = firstname
            user.last_name = lastname
            user.is_active = False
            user.doctor_user.clinic=clinicname
            user.doctor_user.gender=sellist1
            user.save()
            context.update({"requestSend":"Your request is submitted our team will notify you soon"})
        except IntegrityError as e:
            if 'UNIQUE constraint':
                context.update({"error": "Username Already is there try new one"})
                # raise Http404("This User is already registered")
        # do something
    return render(request, "registration/signup.html", context)


def index(request):
    # Create user and save to the database

    return render(request, "ii.html")

def about(request):
    # Create user and save to the database

    return render(request, "about.html")


def Doctor(request):
    # Create user and save to the database

    return render(request, "doctors_list.html")
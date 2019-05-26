from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def index(request,id):
    print('this is id = ',id)
    Doctor_id=User.objects.filter(id=id)
    for i in Doctor_id:
        print(i.get_full_name())
    print('get_full_name() = ',Doctor_id)

    return render(request, 'patient_appointment/appointment.html')



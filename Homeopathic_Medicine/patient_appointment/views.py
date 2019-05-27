from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Appointments
import request


# Create your views here.
def index(request, id):
    print('this is id = ', id)

    context = {
    }

    Doctor_id = User.objects.filter(id=id)
    Doctor = User.objects.get(pk=id)

    for i in Doctor_id:
        print('i.get_full_name(): ', type(i.get_full_name()))
        context.update({'fullname': i.get_full_name()})
    print('get_full_name() = ', Doctor_id)

    if request.method == 'POST':
        phone_num = request.POST.get('Phone')
        email = request.POST.get('email')
        select = request.POST.get('select')
        lastname = request.POST.get('lastname')
        firstname = request.POST.get('firstname')
        Address = request.POST.get('Address')
        msg = request.POST.get('msg')
        appointments = Appointments(doctor_id=id, first_name=firstname, last_name=lastname, address=Address,
                                    phone_num=phone_num,
                                    Gender=select, email=email, Msg=msg)
        appointments.save()
        context.update({'done': 'Your request has been sent to Dr. {}, you will be connected soon by our team'.format(i.get_full_name())})

    return render(request, 'patient_appointment/appointment.html', context)

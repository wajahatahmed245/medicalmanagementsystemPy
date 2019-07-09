import datetime
import json
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from patient.models import Patient, PatientAppointment
from .forms import PatientsManagement
import request
from patient_appointment.models import Appointments
from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from .models import Doctor_User, Visit
from .parts import Face_symptoms_list, head_symptoms_list, Stomach_symptoms_list, Anus_symptoms_list, \
    Circulatory_Organs_symptoms_list, Nose_symptoms_list, Teeth_symptoms_list, limb_symptoms_list, Skin_symptoms_list, \
    Mouth_symptoms_list, Sexual_Organ_symptoms_list, Chest_symptoms_list, appetite_symptoms_list, \
    Generalities_symptoms_list, Female_Sexual_Organs_symptoms_list, Respiratory_Organs_symptoms_list, \
    Heart_symptoms_list, Back_symptoms_list, Sleep_symptoms_list, Mind_symptoms_list
from .machinelearning import predict_medicine


def index(request):
    return render(request, 'Doctor/ii.html')

def Add_to_patients(request,id):

    return render(request, 'Doctor/ii.html')

def appointment_table(request):
    doctor_id = 0
    doctor = User.objects.filter(id=request.user.id)
    for i in doctor:
        doctor_id = i.id
    print(doctor_id)
    patient = PatientAppointment.objects.filter(user=doctor_id).order_by('-id')
    context = {
        'patient': patient
    }

    return render(request, 'Doctor/appointments_table.html', context)


def add_patients(request):
    patient = Patient.objects.all()
    form = PatientsManagement(request.POST or None)
    context = {
        'patient': patient,
        'form': form
    }
    if form.is_valid():
        first_name = form.cleaned_data.get("first_name")
        address = form.cleaned_data.get("address")
        last_name = form.cleaned_data.get("last_name")
        phone_num = form.cleaned_data.get("phone_num")
        email = form.cleaned_data.get("email")
        Gender = form.cleaned_data.get("Gender")

        done = {'result': "patient is added"}
        context.update(done)
        patient_data = Patient(first_name=first_name, last_name=last_name, address=address, phone_num=phone_num,
                               email=email, Gender=Gender)
        patient_data.save()
        doctor_id = 0
        doctor = User.objects.filter(id=request.user.id)
        for i in doctor:
            doctor_id = i.id
        patient_data.user.add(doctor_id)
        print("firstname {} and address is {}".format(first_name, address))
        print("Current User id {}".format(doctor_id))

    return render(request, 'Doctor/add_patients.html', context)


def all_patients(request):
    doctor_id = 0
    doctor = User.objects.filter(id=request.user.id)
    for i in doctor:
        doctor_id = i.id
    print(doctor_id)
    patient = Patient.objects.filter(user=doctor_id).order_by('-id')
    context = {
        'patient': patient
    }
    return render(request, 'Doctor/all_patients.html', context)


def delete_patients(request, id):
    # if request.method == 'POST':
    # get_value = request.body.decode('utf-8')

    # print("get value is = {} ".format(get_value))
    #
    # # print(content)
    # id = int(get_value[3:5])
    # # print()

    Patient.objects.filter(id=id).delete()
    return redirect("/all_patients/")
    # print("the id is {} ".format(id))

    return render(request, 'Doctor/all_patients.html')


def visits(request):
    # if request.method == 'POST':
    # get_value = request.body.decode('utf-8')

    # print("get value is = {} ".format(get_value))
    #
    # # print(content)
    # id = int(get_value[3:5])
    # # print()
    visited_pattients = Visit.objects.all().order_by('-id')
    context = {
        'patients': visited_pattients,
        'Male': 'Male',

    }
    # print("the id is {} ".format(id))

    return render(request, 'Doctor/visit.html', context)


def Appointment_form(request):
    context = {
        # 'appointments': appointments,
        'Male': 'Male'

    }

    if request.method == 'POST':
        context.update({'done': 'Accepted'})
        print("request was = ", request.POST.get('schedule'))
        first_name = request.POST.get("first_name")
        address = request.POST.get("address")
        last_name = request.POST.get("last_name")
        phone_num = request.POST.get("phone_num")
        email = request.POST.get("email")
        Gender = request.POST.get("Gender")

        # print('hello')
        # x = datetime.datetime()
        print(type(request.POST.get('schedule')))
        date = request.POST.get('schedule')
        date_in = request.POST.get('schedule')
        patient_data = PatientAppointment(first_name=first_name, last_name=last_name, address=address,
                                          phone_num=phone_num,
                                          email=email, Gender=Gender, Datetime=date)
        patient_data.save()
        doctor_id = 0
        doctor = User.objects.filter(id=request.user.id)
        for i in doctor:
            doctor_id = i.id
        patient_data.user.add(doctor_id)
        date_out = datetime.datetime(*[int(v) for v in date_in.replace('T', '-').replace(':', '-').split('-')])
        print(date_out)
    # if request.method == 'POST':
    # get_value = request.body.decode('utf-8')

    # print("get value is = {} ".format(get_value))
    #
    # # print(content)
    # id = int(get_value[3:5])
    # # print()
    print('hello')
    # id = request.user.id
    # appointments = Appointments.objects.filter(doctor_id=id)

    # print("the id is {} ".format(id))

    return render(request, 'Doctor/appontment_form.html', context)


def appointments_patients(request):
    # if request.method == 'POST':
    # get_value = request.body.decode('utf-8')

    # print("get value is = {} ".format(get_value))
    #
    # # print(content)
    # id = int(get_value[3:5])
    # # print()
    id = request.user.id
    appointments = Appointments.objects.filter(doctor_id=id)
    context = {
        'appointments': appointments,
        'Male': 'Male'

    }
    # print("the id is {} ".format(id))

    return render(request, 'Doctor/appointments.html', context)


def update_patient(request, id):
    if request.method == 'POST':
        print("wajahat")
        print(request.POST.get('pswd'))
        update_patient_key = Patient.objects.get(id=id)
        update_patient_key.phone_num = request.POST.get('pswd')
        update_patient_key.address = request.POST.get('Address')
        update_patient_key.last_name = request.POST.get('Last_Name')
        update_patient_key.first_name = request.POST.get('first_name')
        update_patient_key.Gender = request.POST.get('gender')

        update_patient_key.save()
        return redirect("/all_patients/")
    patient_update = Patient.objects.filter(id=id)
    context = {
        'patient': patient_update
    }
    return render(request, 'Doctor/update_patient.html', context)


def examine(request, id):
    context = {
        'head': head_symptoms_list,
        'Stomach_symptoms_list': Stomach_symptoms_list,
        'Face_symptoms_list': Face_symptoms_list,
        'Anus_symptoms_list': Anus_symptoms_list,
        'Circulatory_Organs_symptoms_list': Circulatory_Organs_symptoms_list,
        'Nose_symptoms_list': Nose_symptoms_list,
        'Teeth_symptoms_list': Teeth_symptoms_list,
        'limb_symptoms_list': limb_symptoms_list,
        'Skin_symptoms_list': Skin_symptoms_list,
        'Mouth_symptoms_list': Mouth_symptoms_list,
        'Sexual_Organ_symptoms_list': Sexual_Organ_symptoms_list,
        'Chest_symptoms_list': Chest_symptoms_list,
        'appetite_symptoms_list': appetite_symptoms_list,
        'Generalities_symptoms_list': Generalities_symptoms_list,
        'Female_Sexual_Organs_symptoms_list': Female_Sexual_Organs_symptoms_list,
        'Respiratory_Organs_symptoms_list': Respiratory_Organs_symptoms_list,
        'Heart_symptoms_list': Heart_symptoms_list,
        'Back_symptoms_list': Back_symptoms_list,
        'Sleep_symptoms_list': Sleep_symptoms_list,
        'Mind_symptoms_list': Mind_symptoms_list
    }
    if request.method == 'POST':
        print('num2 : ', request.POST.get('op1'))
        print('num3 : ', request.POST.get('op2'))
        symptopms_selected = ' '
        symptopms_selected_print_secreen = ''
        symptoms_all = sum([head_symptoms_list, Stomach_symptoms_list, Face_symptoms_list, Anus_symptoms_list,
                            Circulatory_Organs_symptoms_list, Nose_symptoms_list, Teeth_symptoms_list,
                            limb_symptoms_list, Skin_symptoms_list, Mouth_symptoms_list, Sexual_Organ_symptoms_list,
                            appetite_symptoms_list, Generalities_symptoms_list, Female_Sexual_Organs_symptoms_list,
                            Respiratory_Organs_symptoms_list, Heart_symptoms_list, Back_symptoms_list,
                            Sleep_symptoms_list, Mind_symptoms_list], [])
        print(len(symptoms_all))
        for i in range(0, len(symptoms_all)):
            if request.POST.get(symptoms_all[i]) != None:
                print('the {} and post is {} '.format(symptoms_all[i], request.POST.get(symptoms_all[i])))
                symptopms_selected += ' ' + symptoms_all[i]
                symptopms_selected_print_secreen += ',' + symptoms_all[i]
                # symptopms_selected.append(symptoms_all[i])
        print('lis : ', symptopms_selected)
        predict = predict_medicine(symptopms_selected)

        print(predict)
        Doctor_who_is_examining = request.user.id
        patient_treated = id
        Doctor_u = User.objects.get(pk=Doctor_who_is_examining)
        Patient_c = Patient.objects.get(pk=patient_treated)

        Visit_table = Visit(doctor=Doctor_u, patient=Patient_c, symptoms=symptopms_selected_print_secreen[1:],
                            symptomsMedicine=str(predict)[2:-2])
        Visit_table.save()
        context.update({'Visit_table_id': Visit_table.id})
        print("Visit_table id : ", Visit_table.id)

        print("predict: ", str(predict))

        print('selected : ', type(symptopms_selected_print_secreen))

    return render(request, 'Doctor/examine.html', context)


def next_examine(request, id):
    Visited_patient = Visit.objects.get(pk=id)

    context = {
        'name': Visited_patient.patient.first_name + ' ' + Visited_patient.patient.last_name,
        'address': Visited_patient.patient.address,
        'phone_num': Visited_patient.patient.phone_num,
        'symptoms': Visited_patient.symptoms,
        'symptomsMedicine': Visited_patient.symptomsMedicine,

    }
    if request.method == 'POST':
        print('extramedicine : ', type(request.POST.get('extramedicine')))
        Visited_patient.extraMediceine = request.POST.get('extramedicine')
        Visited_patient.save()
        context.update({'success': 'Extra Medicine is added Click on print to for receipt',
                        'extramedicine': Visited_patient.extraMediceine})

    return render(request, 'Doctor/examine_next.html', context)


class DoctorInfo(generic.ListView):
    template_name = 'Doctor/doc_list.html'
    context_object_name = 'Doc_list'

    def get_queryset(self):
        return Doctor_User.objects.all()


def test(request):
    context = {
        'head': head_symptoms_list,
        'Stomach_symptoms_list': Stomach_symptoms_list,
        'Face_symptoms_list': Face_symptoms_list,
        'Anus_symptoms_list': Anus_symptoms_list,
        'Circulatory_Organs_symptoms_list': Circulatory_Organs_symptoms_list,
        'Nose_symptoms_list': Nose_symptoms_list,
        'Teeth_symptoms_list': Teeth_symptoms_list,
        'limb_symptoms_list': limb_symptoms_list,
        'Skin_symptoms_list': Skin_symptoms_list,
        'Mouth_symptoms_list': Mouth_symptoms_list,
        'Sexual_Organ_symptoms_list': Sexual_Organ_symptoms_list,
        'Chest_symptoms_list': Chest_symptoms_list,
        'appetite_symptoms_list': appetite_symptoms_list,
        'Generalities_symptoms_list': Generalities_symptoms_list,
        'Female_Sexual_Organs_symptoms_list': Female_Sexual_Organs_symptoms_list,
        'Respiratory_Organs_symptoms_list': Respiratory_Organs_symptoms_list,
        'Heart_symptoms_list': Heart_symptoms_list,
        'Back_symptoms_list': Back_symptoms_list,
        'Sleep_symptoms_list': Sleep_symptoms_list,
        'Mind_symptoms_list': Mind_symptoms_list

    }
    if request.method == 'POST':
        print('num2 : ', request.POST.get('op1'))
        print('num3 : ', request.POST.get('op2'))
        symptopms_selected = ' '

        symptoms_all = sum([head_symptoms_list, Stomach_symptoms_list, Face_symptoms_list, Anus_symptoms_list,
                            Circulatory_Organs_symptoms_list, Nose_symptoms_list, Teeth_symptoms_list,
                            limb_symptoms_list, Skin_symptoms_list, Mouth_symptoms_list, Sexual_Organ_symptoms_list,
                            appetite_symptoms_list, Generalities_symptoms_list, Female_Sexual_Organs_symptoms_list,
                            Respiratory_Organs_symptoms_list, Heart_symptoms_list, Back_symptoms_list,
                            Sleep_symptoms_list, Mind_symptoms_list], [])
        print(len(symptoms_all))
        for i in range(0, len(symptoms_all)):
            if request.POST.get(symptoms_all[i]) != None:
                print('the {} and post is {} '.format(symptoms_all[i], request.POST.get(symptoms_all[i])))
                symptopms_selected += ' ' + symptoms_all[i]
                # symptopms_selected.append(symptoms_all[i])
        print('lis : ', symptopms_selected)
        predict = predict_medicine(symptopms_selected)
        print(predict)
    return render(request, 'Doctor/submit_test.html', context)

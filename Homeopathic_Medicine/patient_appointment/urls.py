from django.urls import path

from . import views
app_name = 'Patient_Appointment'

urlpatterns = [

    path('appointment/', views.index, name='appointment'),


]
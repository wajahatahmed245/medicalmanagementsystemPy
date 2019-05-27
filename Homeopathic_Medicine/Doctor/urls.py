from django.urls import path

from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_patients/', views.add_patients, name='add_patients'),
    path('all_patients/', views.all_patients, name='all_patients'),
    path('del_patients/<int:id>/', views.delete_patients, name='delete_patient'),
    path('update_patient/<int:id>/', views.update_patient, name='update_patient'),
    path('Doctors', views.update_patient, name='update_patient'),
    path('visits/', views.visits, name='visits'),
    path('appointments/', views.appointments_patients, name='appointmments'),
    path('examine/<int:id>/', views.examine, name='examine'),
    path('examine_next/<int:id>/', views.next_examine, name='examine_next'),

    path('submittest/', views.test),

]
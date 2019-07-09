from django.contrib import admin
from .models import Patient,PatientAppointment


# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'symptoms', 'medicine', 'created_at')

    def user(self, obj):
        return obj.fisrtname


admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientAppointment)


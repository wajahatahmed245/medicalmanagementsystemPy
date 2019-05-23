from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'phone_num')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['isa'] = instance.isa()
        data['curent'] = instance.curent()
        return data

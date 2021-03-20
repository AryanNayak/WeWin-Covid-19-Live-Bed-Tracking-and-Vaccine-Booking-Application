from rest_framework import serializers
from .models import Hospitals,  Patient, State


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
    
        model = Hospitals
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'





class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

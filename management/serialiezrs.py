from rest_framework import serializers
from management.models import Directors, Employees, OTMLeaders, EOLeaders, PELeaders


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directors
        fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class OTMLeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTMLeaders
        fields = '__all__'


class EOLeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EOLeaders
        fields = '__all__'


class PELeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PELeaders
        fields = '__all__'


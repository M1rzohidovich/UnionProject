from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Directors, Employees, PELeaders, OTMLeaders, EOLeaders
from .serialiezrs import DirectorSerializer, EmployeesSerializer, OTMLeadersSerializer, \
    PELeadersSerializer, EOLeadersSerializer


class GetDirector(APIView):

    def get(self, request):
        director = Directors.objects.all()
        serializer = DirectorSerializer(director, many=True)

        return Response(serializer.data)


class GetEmployees(APIView):

    def get(self, request):
        emp = Employees.objects.all()
        serializer = EmployeesSerializer(emp, many=True)

        return Response(serializer.data)


class GetOTMLeaders(APIView):

    def get(self, request):
        otm = OTMLeaders.objects.all()
        serializer = OTMLeadersSerializer(otm, many=True)

        return Response(serializer.data)


class GetEOLeaders(APIView):

    def get(self, request):
        eo = EOLeaders.objects.all()
        serializer = EOLeadersSerializer(eo, many=True)

        return Response(serializer.data)


class GetPELeaders(APIView):

    def get(self,request):
        pe = PELeaders.objects.all()
        serializer = PELeadersSerializer(pe, many=True)

        return Response(serializer.data)



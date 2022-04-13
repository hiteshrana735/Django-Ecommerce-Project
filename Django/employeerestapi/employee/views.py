from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework import status

# Create your views here.
class EmployeeAPI(APIView):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({"status" : "suceess", "data" : serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success", "data" : serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response({"status" : "Error Occured", "data" : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



# {
# "name":"Haaris",
# "deptt":"Finance",
# "address":"Delhi"
# }
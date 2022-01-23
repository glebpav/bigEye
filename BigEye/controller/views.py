from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.


class EmployeeView(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({"employees": serializer.data})

    def post(self, request):
        employee = request.data.get('employee')
        serializer = EmployeeSerializer(data=employee)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' created successfully".format(employee_saved.fio)})

    def put(self, request, pk):
        saved_employee = get_object_or_404(Employee.objects.all(), pk=pk)
        data = request.data.get('employee')
        serializer = EmployeeSerializer(instance=saved_employee, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_employee = serializer.save()
        return Response({
            "success": "Employee '{}' updated successfully".format(saved_employee.fio)
        })

    def delete(self, request, pk):
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        employee.delete()
        return Response({
            "message": "Employee with id `{}` has been deleted.".format(pk)
        }, status=204)


class DataCollectionView(APIView):
    def get(self, request):
        dataCollection = DataCollection.objects.all()
        serializer = DataCollectionSerializer(dataCollection, many=True)
        return Response({"dataCollection": serializer.data})

    def post(self, request):
        dataCollection = request.data.get('dataCollection')
        serializer = DataCollectionSerializer(data=dataCollection)
        if serializer.is_valid(raise_exception=True):
            dataCollection = serializer.save()
        return Response({"success": "DataCollection '{}' created successfully".format(dataCollection.rating)})

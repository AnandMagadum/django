from django.shortcuts import render
from rest_framework import viewsets
from company.models import Company,Employee
from company.serializers import companySerializer,employeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CompanyViewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=companySerializer
    
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=1):
        
        # comp=Company.objects.get(ID=pk)
        # print(comp)
        employees=Employee.objects.filter(Company_Id=pk)
        print(employees)
        empser=employeeSerializer(employees,many=True,context={"request":request})
        return Response(empser.data)
# Create your views here.

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=employeeSerializer
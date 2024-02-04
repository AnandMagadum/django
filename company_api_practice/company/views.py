from django.shortcuts import render
from rest_framework import viewsets
from company.models import Company,Employee
from company.serializers import companySerializer,employeeSerializer,CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.parsers import JSONParser


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

def company(request):
    #print(model_to_dict(Company.objects.all()))
    ser=CompanySerializer(Company.objects.all(),many=True)
    # print(Company.objects.get(ID=1).__dict__)
    # print(ser.data)
    #print(Company.objects.all())
    #print(ser.is_valid())
    print(ser.data)
    
    return JsonResponse(ser.data,safe=False)

@csrf_exempt
def employee(request,pk):

    try:
        dataes=Employee.objects.get(pk=pk)
    except Exception as e:
        return HttpResponse(status=404)
    
    if request.method=="GET":
        ser=EmployeeSerializer(dataes)
        return JsonResponse(ser.data)
    
    if request.method=="PUT":
        datatomod=JSONParser().parse(request)
        ser=EmployeeSerializer(dataes,data=datatomod)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201)
        return JsonResponse(ser.errors,status=400)
    
    if request.method=="DELETE":
        dataes.delete()
        return HttpResponse(status=204)
    
class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=employeeSerializer
from django.shortcuts import render
from rest_framework import viewsets
from company.models import Company,Employee
from company.serializers import companySerializer,employeeSerializer,CompanySerializer,EmployeeSerializer,UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views import generic
from django.contrib.auth.models import User


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
@csrf_exempt
@api_view(["GET","POST"])
def company(request):
    
    if request.method=="GET":
        try:
            #print(model_to_dict(Company.objects.all()))
            ser=CompanySerializer(Company.objects.all(),many=True)
            # print(Company.objects.get(ID=1).__dict__)
            # print(ser.data)
            #print(Company.objects.all())
            #print(ser.is_valid())
            print(ser.data)
            return JsonResponse(ser.data,safe=False)
        except Exception as e:
            return JsonResponse({"msg":str(e)+"Please report this error to admin through email admin abc@gmaail.com"},status=400)
    if request.method=="POST":
        ser=CompanySerializer(data=request.data)
        #ser.create(request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201)
        
@api_view(["PUT","GET","DELETE"])
@csrf_exempt
def company_query(request,pk):
    print("Hello")
    det=Company.objects.get(pk=pk)
    det2=Company.objects.filter(ID=pk)
    print(det)
    print(det2)
    cmpnmae=det2[0].Name
    if request.method=="PUT":
        ser=CompanySerializer(det,data=request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data)
        return JsonResponse(status=400)
    
    if request.method == "DELETE":
        det.delete()
        return JsonResponse({"msg":f"Deleted comapny {cmpnmae}"},status=204)
            
@csrf_exempt
@api_view(["GET","DELETE","PUT"])
def employee(request,pk):

    try:
        dataes=Employee.objects.get(pk=pk)
    except Exception as e:
        return HttpResponse(status=404)
    
    if request.method=="GET":
        ser=EmployeeSerializer(dataes)
        print(ser.data)
        return JsonResponse(ser.data)
    
    if request.method=="PUT":
        print(request)
        print(request.user)
        print(request.data)
        # datatomod=JSONParser().parse(request)
        # print("datammod",datatomod)
        # print("datammod",datatomod)
        ser=EmployeeSerializer(dataes,data=request.data)
        print(ser)
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
    
class userslist(generic.ListView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    

class userdetails(generic.RedirectView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
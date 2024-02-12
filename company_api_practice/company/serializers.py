from rest_framework import serializers
from company import models
from company.models import company_choices,employee_choices,Company
from django.contrib.auth.models import User

class companySerializer(serializers.HyperlinkedModelSerializer):
    ID=serializers.ReadOnlyField()
    class Meta:
        model=models.Company
        fields="__all__"
        
class employeeSerializer(serializers.HyperlinkedModelSerializer):
    Emp_ID=serializers.ReadOnlyField()
    class Meta:
        model=models.Employee
        fields="__all__"


# creating custom made serializer for company model        
class CompanySerializer(serializers.Serializer):
    #ID=serializers.ReadOnlyField()
    ID=serializers.IntegerField(read_only=True,)
    Name=serializers.CharField(max_length=100)
    Type=serializers.ChoiceField(choices=company_choices,default='IT')
    FoundedDate=serializers.DateField()
    Founder=serializers.CharField()
    About=serializers.CharField(style={'base_template':'textarea.html'},allow_blank=True)
    Address=serializers.CharField()
    Updated=serializers.DateTimeField()
    
    def create(self,validated_data):
        return Company.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        #hello
        instance.Name=validated_data.get('Name',instance.Name)
        instance.Type=validated_data.get('Type',instance.Type)
        instance.FoundedDate=validated_data.get('FoundedDate',instance.FoundedDate)
        instance.Founder=validated_data.get('Founder',instance.Founder)
        instance.About=validated_data.get('About',instance.About)
        instance.Address=validated_data.get('Address',instance.Address)
        instance.save()
        return instance
    
class EmployeeSerializer(serializers.ModelSerializer):
        Emp_ID=serializers.ReadOnlyField()
        class Meta:
            model=models.Employee
            fields="__all__"
    
        
        
class UserSerializer(serializers.ModelSerializer):
    Companys=serializers.PrimaryKeyRelatedField(many=True,queryset=User.objects.all())
    class Meta:
        model=User
        fields="__all__"
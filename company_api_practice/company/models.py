from django.db import models
import datetime
import django
# Create your models here.

##company_choices
company_choices=(('Information Technology','IT'),
                                                 ('Manufacturing Industry','Manufacturing'),
                                                 ("Transport",'Transport'),
                                                 ('Service','Service'))

##Employee  Choices
employee_choices=(('Deliver Manager','DM'),
                                        ('Project Manager','PM'),
                                        ('Team Manager','TM'),
                                        ("Team Lead",'TL'),
                                        ('Engineer','Engineer'))

class Company(models.Model):
    ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Type=models.CharField(max_length=50,choices=company_choices)
    FoundedDate=models.DateField()
    Founder=models.CharField(max_length=100)
    About=models.TextField(null=True)
    Address=models.TextField()
    Updated=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey('auth.User',related_name="Companys",on_delete=models.CASCADE)
    def __str__(self):
        return str(self.ID)
    
class Employee(models.Model):
    Emp_ID=models.AutoField(primary_key=True)
    Company_Id=models.ForeignKey(Company,on_delete=models.CASCADE)
    Emp_Name=models.CharField(max_length=10)
    Emp_Designation=models.CharField(max_length=50,choices=employee_choices)
    Emp_Address=models.TextField()
    Emp_DOB=models.DateField()
    Emp_DOJ=models.DateField()
    Emp_Skills=models.TextField()
    Emp_Update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Emp_Name
    
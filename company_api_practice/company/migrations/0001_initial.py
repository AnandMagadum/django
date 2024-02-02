# Generated by Django 4.2 on 2024-02-01 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Type', models.CharField(choices=[('Information Technology', 'IT'), ('Manufacturing Industry', 'Manufacturing'), ('Transport', 'Transport'), ('Service', 'Service')], max_length=50)),
                ('FoundedDate', models.DateField()),
                ('Founder', models.CharField(max_length=100)),
                ('About', models.TextField()),
                ('Address', models.TextField()),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Emp_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Emp_Name', models.CharField(max_length=10)),
                ('Emp_Designation', models.CharField(choices=[('Deliver Manager', 'DM'), ('Project Manager', 'PM'), ('Team Manager', 'TM'), ('Team Lead', 'TL'), ('Engineer', 'Engineer')], max_length=50)),
                ('Emp_Address', models.TextField()),
                ('Emp_DOB', models.DateField()),
                ('Emp_DOJ', models.DateField()),
                ('Emp_Skills', models.TextField()),
                ('Emp_Update', models.DateTimeField(auto_now=True)),
                ('Company_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]

from django.db import models

# Create your models here.

class Department(models.Model):
    department_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)  # Head of Department
    start_date = models.DateField()
    no_of_students = models.IntegerField()
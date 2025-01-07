from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class RegisterUsers(AbstractUser):
    emp_id=models.IntegerField(unique=True)
    emp_name=models.CharField(max_length=255)
    emp_email=models.CharField(max_length=255,unique=True)
    emp_department=models.CharField(max_length=25)
    emp_role=models.CharField(max_length=30)
    emp_phn_number=models.CharField(max_length=30,unique=True)
    password1=models.CharField(max_length=255,unique=True)
    password1=models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.emp_id,self.emp_name,self.emp_role


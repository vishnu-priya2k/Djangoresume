from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    phno=models.IntegerField()
    st = models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    pincode = models.IntegerField()

class Meta:
    db_table = 'student'
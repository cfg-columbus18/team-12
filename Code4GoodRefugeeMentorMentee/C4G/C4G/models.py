from django.db import models

class Student(models.Model):
    firstName= models.CharField(max_length=30),
    lastName= models.CharField(max_length=30),



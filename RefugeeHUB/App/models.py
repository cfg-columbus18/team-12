from django.db import models

class Student(models.Model):
    userID= models.IntegerField(),
    firstName= models.CharField(max_length=30)
    lastName= models.CharField(max_length=30)
    phoneNumber= models.CharField(max_length=16)
    email=models.CharField(max_length=30)
    bio = models.CharField(max_length=500)
    language = models.CharField(max_length=500)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    ref_Region= models.CharField(max_length=30)
    ref_language= models.CharField(max_length=30)
    ref_reason =  models.CharField(max_length=300)
    isTeacher = models.BooleanField()
    skill1 = models.CharField(max_length=30)
    skill2 = models.CharField(max_length=30)
    skill3 = models.CharField(max_length=30)
    commPref = models.CharField(max_length=30)
    commPref2 = models.CharField(max_length=30)
    commPref3= models.CharField(max_length=30)

    


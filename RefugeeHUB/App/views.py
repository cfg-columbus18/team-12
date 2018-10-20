from django.http import HttpResponse
from RefugeeHUB.models import Student


def index(request):
   
    return HttpResponse("Hello, world. You're at the polls index.")

def getStudent(request):
    print(request.GET)
    student = Student.objects.all()
    jane = Student.objects.create(firstName='Janes', lastName='cook')
    jane.save()
    print(student)

    return HttpResponse("Done")
    
 

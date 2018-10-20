from django.http import HttpResponse
from C4G.models import Student


def index(request):
   
    return HttpResponse("Hello, world. You're at the polls index.")

def getStudent(request):
    student = Student.objects.all()
    jane = Student.objects.create(firstName='Janes', lastName='cook')
    jane.save()
    print(student)

    return HttpResponse("Done")
    
 

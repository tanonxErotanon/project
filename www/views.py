from django.shortcuts import render
from .models import *

def index(request):
    students_list = Student.objects.all()


    context ={
        "list":students_list,
        "number":students_list.count()
    }
    return render(request,"index.html",context)
def r(request):
    students_list = Student.objects.all()


    context ={
        "list":students_list,
        "number":students_list.count()
    }
    return render(request,"r.html",context)
   
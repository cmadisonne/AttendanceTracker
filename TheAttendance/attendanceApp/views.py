from django.shortcuts import render
from .models import attendanceModel


def index(request):
    students = attendanceModel.objects.all()
    context = {'students': students}
    return render(request, 'attendanceApp/index.html', context)




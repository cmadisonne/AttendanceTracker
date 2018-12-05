from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import attendanceModel
from .forms import clockInForm, clockOutForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    students = attendanceModel.objects.all()
    context = {'students': students}
    return render(request, 'attendanceApp/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
        return render(request, 'attendanceApp/signUp.html', {'form': form})

def clockIn(request,pk):
    student_instance = get_object_or_404(attendanceModel, pk=pk)
    if request.method == 'POST':
        form = clockInForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            return redirect('index')
    else:
        form = clockInForm()
        return render(request, 'attendanceApp/clockIn.html', {'form':form})

def clockOut(request,pk):
    if request.method == 'POST':
        form = clockOutForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            return redirect('index')
    else:
        form = clockOutForm()
        return render(request, 'attendanceApp/clockOut.html', {'form':form})
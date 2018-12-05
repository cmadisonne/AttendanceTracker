from django.shortcuts import render, redirect, get_object_or_404
from .models import attendanceModel
from .forms import clockInForm, clockOutForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    students = attendanceModel.objects.all()
    context = {'students': students}
    return render(request, 'attendanceApp/index.html', context)

def clockIn(request):
    print("In the first 'If'")
    if request.method == 'POST':
        form = clockInForm(request.POST)
        print(form)
        print("Returned in the first if")
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.username = request.user
            newForm.save()
            print("returned after the save")
            return redirect('index')
    else:
        form = clockInForm()
        print("returned in the ELSE")
        return render(request, 'attendanceApp/clockIn.html', {'form':form})

def clockOut(request):
    if request.method == 'POST':
        form = clockOutForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            return redirect('index')
    else:
        form = clockOutForm()
        return render(request, 'attendanceApp/clockOut.html', {'form':form})


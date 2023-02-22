from django.shortcuts import render, redirect
from .models import Department, Course
from django.http import JsonResponse

# Create your views here.
def home (request):
    return render(request,'base.html')
def login(request):
    if request.method == "POST":
        return redirect('/')
    return render(request,'login.html')
def register(request):
    if request.method == "POST":
        return redirect('/')
    return render(request, 'register.html')
def registerform(request):
    qs=Department.objects.all()
    qs1 = Course.objects.all()
    return render(request,'registerform.html',{'qs':qs,'qs1':qs1})
def firstregister(request):
    return render(request,'firstregister.html')
def get_json(request):
    qsval = list(Department.objects.values())
    return JsonResponse({'data':qsval})

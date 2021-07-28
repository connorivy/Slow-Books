from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def employees(request):
    return render(request,'dashboard/employees.html')

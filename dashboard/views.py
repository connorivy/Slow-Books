from django.shortcuts import render, redirect
from django.contrib import messages
from .models import employee
from .forms import addEmployee

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def employees(request):
    if request.method == 'POST':
        form = addEmployee(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            messages.success(request, f'{fname} {lname} added to employees')
            # return redirect('dashboard-employees')
    else:
        form = addEmployee()

    context = {
        'form': form,
        'employees': employee.objects.all().values()
    }
    print(context['employees'])

    return render(request, 'dashboard/employees.html', context)
    # return render(request, 'dashboard/employees.html')
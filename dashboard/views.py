from django.shortcuts import render
from .models import employees
from .forms import addEmployee

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def employees(request):
    if request.method == 'POST':
        form = addEmployee(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('dashboard-home')
    else:
        form = addEmployee()

    return render(request, 'dashboard/employees.html', {'form': form})
    # return render(request, 'dashboard/employees.html')

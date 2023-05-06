from django.shortcuts import render
from  django.http import HttpResponse
from django.shortcuts import reverse, redirect
from employees.models import Employee
from employees.forms import EmployeeForm

# Create your views here.
def list_employees(request):
    employees = Employee.get_all_employees()
    return render(request, 'employee/list.html', {"emps": employees})

def get_employee(request, id):
    employee = Employee.get_employee(id)
    return render(request, 'employee/show.html', {"emp": employee})

def delete_employee(request, id):
    Employee.delete_employee(id)
    redirect_url = reverse('list_employees')
    return redirect(redirect_url)

# def create_employee(request):
#     return HttpResponse(f"create new employee")

# def edit_employee(request, id ):
#     return HttpResponse(f"edit employee")

def create_employee(request):
    if request.method =='GET':
        form  = EmployeeForm()
        return render(request, 'employee/create.html', context={"form":form})
    else:
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        redirect_url = reverse('list_employees')
        return redirect(redirect_url)

def edit_employee(request, id ):
    employee = Employee.get_employee(id)
    if request.method =='GET':
        form = EmployeeForm(instance=employee)
        return render(request, 'employee/edit.html', context={"form":form})
    else:
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
        redirect_url = reverse('get_employee',args=[employee.id])
        return redirect(redirect_url)
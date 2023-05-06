from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def employees(request):
    emps = ["khaled", "ahmed", "aya", "arwa"] 
    return render(request, 'employees.html', context={"employees": emps})

def about(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contact.html')
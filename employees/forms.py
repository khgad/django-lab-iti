from django import forms
from employees.models import Employee

""" create form based on the model"""
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
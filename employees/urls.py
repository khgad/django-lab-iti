from django.urls import path, include
from .views import *

urlpatterns = [
    path('', list_employees, name='list_employees'),
    path('<int:id>', get_employee, name='get_employee'),
    path('<int:id>/edit', edit_employee, name='edit_employee'),
    path('<int:id>/delete', delete_employee, name='delete_employee'),
    path('create', create_employee, name='create_employee'),
]

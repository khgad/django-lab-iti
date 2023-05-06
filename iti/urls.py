from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('employees', employees, name='employees'),
    path('about', about, name='about'),
    path('contact', contactus, name='contact'),
]

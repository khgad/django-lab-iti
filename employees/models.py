from django.db import models
from django.shortcuts import reverse
from departments.models import Department

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    salary = models.IntegerField(default=5000)
    image = models.ImageField(upload_to='employee/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    dept = models.ForeignKey(Department, null=True, blank=True,
                             on_delete=models.CASCADE, related_name='dept_employees')

    def __str__(self):
        return self.name

    @classmethod
    def get_all_employees(cls):
        return cls.objects.all()

    @classmethod
    def get_employee(cls, id):
        return cls.objects.get(id=id)
    
    @classmethod
    def delete_employee(cls, id):
        employee = cls.get_employee(id)
        return employee.delete()

    def get_delete_url(self):
        delete_url = reverse('delete_employee',args=[self.id])
        return delete_url

    def get_show_url(self):
        show_url = reverse('get_employee',args=[self.id])
        return show_url


    def get_image_url(self):
        return f"/media/{self.image}"


    def get_edit_url(self):
        edit_url = reverse('edit_employee',args=[self.id])
        return edit_url

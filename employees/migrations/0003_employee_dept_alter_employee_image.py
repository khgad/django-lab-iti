# Generated by Django 4.2.1 on 2023-05-06 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
        ('employees', '0002_employee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_employees', to='departments.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='employee/'),
        ),
    ]
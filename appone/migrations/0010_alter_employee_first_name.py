# Generated by Django 4.0.6 on 2022-07-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0009_rename_dept_employee_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_alter_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0003_alter_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
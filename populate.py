import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'office_emp_mgmt.settings')

import django
django.setup()

#population start
import random
from faker import Faker
from appone.models import Role, Department, Employee
from datetime import date

fakegen = Faker()


def department():
    depts = ["HR", "Technical", "Sales", "Storage", "Electrical", "Communications", "Hiring", "Accounts", "Management"]
    # city = fakegen.city()

    t = Department.objects.get_or_create(name=random.choice(depts))[0]
    t.save()
    return t

def role():
    job = fakegen.job()
    t = Role.objects.get_or_create(name=job)[0]
    t.save()
    return t


def populate(n=5):
    for i in range(n):
        dept = department()
        role_obj = role()

        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        phone = fakegen.phone_number()

        employee_rec = Employee.objects.get_or_create(first_name=first_name, last_name=last_name, department=dept, role=role_obj, phone=phone, hire_date=date.today())


if __name__ == "__main__":
    n = int(input("enter the number of fake records: "))
    print("populating...")
    populate(n)
    print("population done!!!")
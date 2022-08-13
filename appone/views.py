from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from datetime import date
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request, 'index.html')


def view_emp(request):
    model = Employee.objects.all()
    return render(request, 'view_emp.html', {'model' : model})

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = int(request.POST['department'])
        salary = int(request.POST['salary'])
        role = int(request.POST['role'])
        phone = request.POST['phone']
        bonus = int(request.POST['bonus'])

        obj = Employee(first_name=first_name, last_name=last_name, department_id=department, role_id=role, phone=phone, bonus=bonus, hire_date=date.today())
        obj.save()
        return render(request, 'employee_added.html')

    elif request.method == "GET":
        return render(request, 'add_emp.html')

    else:
        return HttpResponse("An exception occurred! Employee not added!")

def remove_emp(request, emp_id=0):
    if emp_id:
        # try:
        employee = Employee.objects.get(id=emp_id)
        employee.delete()
        return view_emp(request)
        # except:
        #     return HttpResponse("<h1>Employee not found!!!</h1>")

    model = Employee.objects.all()
    return render(request, 'remove_emp.html', {'model' : model})


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        role = request.POST['role']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))

        if department:
            emps = emps.filter(department__name = department)

        if role:
            emps = emps.filter(role__name = name)

        return render(request, 'view_emp.html', {'model' : emps})

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')

    return HttpResponse("<h1>An error occurred</h1>")
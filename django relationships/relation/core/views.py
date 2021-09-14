from django.shortcuts import render
from . models import Department, Employee, User, Phone, Book, Store
from django.http import HttpResponse
# Create your views here.


def index(request):
    
    # without relationship:
    user = User.objects.get(pk=1)
    phone = Phone.objects.get(user_id=user)
    
    
    
    # with relationship:
    # related to the model Phone
    # user = User.objects.get(pk=1).phone
    
    # using related_name = "number"
    # returning object
    user_phone = User.objects.get(pk=1).number
    # returning string
    user_phone_str = User.objects.get(pk=1).number.phone_no
    print("--------------------------------------")
    print(user_phone)
    
    
    # reverse geting user from phone
    user = Phone.objects.get(id=1).user_id
    
    return HttpResponse(user)


def foreign_key(request):
    
    # using REVERSE !!!IMPORTANT!!! 
    user = Employee.objects.get(name="Simpson").department_name
    user = Employee.objects.get(name="Simpson").department_name.name        
    # print(user)
    # print(type(user))
    
    first_deparment = Department.objects.get(pk=1) #hr
    second_deparment = Department.objects.get(pk=2) #accouts
    third_deparment = Department.objects.get(pk=5) #purchase
    
    deparments = Employee.objects.filter(department_name=third_deparment)
    
    # related name !!! IMPORTANT!!!  -- another way employee_set.all() -- doesnt work
    employees_from_dep = first_deparment.employeees_rel.all()
    employees_from_dep = first_deparment.employeees_rel.all().filter()
    #print(employees_from_dep)
    
    # related name !!! IMPORTANT!!! 
    # after rel name __double underscore through which i can manipulate others model fields
    dep_all_empl = Department.objects.all().filter(employeees_rel__name__startswith="John")    
    
    #if there is NO related name it will work next line will work with name of model
    #dep_all_empl = Department.objects.all().filter(employee__name__startswith="John")
    
    # reverse !!!!!!! VERY IMPORTANT !!!!!!
    employees_in_HR = Employee.objects.filter(department_name__name='Accounts')
    
    print(employees_in_HR)
    
    return HttpResponse(employees_in_HR)


# select_related
# https://docs.djangoproject.com/en/3.0/ref/models/querysets/#select-related
def sel_related(request):
    
    # fetching all employees and printing their names #INNER join
    employees = Employee.objects.all().select_related('department_name')
    
    #employees = Employee.objects.all()
    for i in employees:
        print(i.name, i.department_name.name)
    
    return render(request, 'core/stuff.html')
        

# for debuger
def users(request):
    qs = User.objects.all()    
    return render(request, 'core/users.html',{
        "users": qs,
    })
    
    
def prefetched(request):
    books = Book.objects.all()
    books = Book.objects.all().prefetch_related('store_set')
    
    #looking for all STORES and check THIS BOOK in it
    for i in books:        
        print(i.store_set.all())
    
    return render(request, 'core/users.html')

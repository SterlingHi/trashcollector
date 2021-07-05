from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
# Create your views here.
from django.contrib.auth.models import Group


# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    return render(request, 'customers/index.html')


def weekly(request):
    user = request.user
    print(user)
    return render(request, 'customers/weekly.html')


def onetime(request):
    return render(request, 'customers/onetime.html')


def suspend(request):
    return render(request, 'customers/suspend.html')


def balance(request):
    user = request.user
    print(user)
    return render(request, 'customers/balance.html')

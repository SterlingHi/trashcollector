from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from django.urls import reverse
# Create your views here.
from django.contrib.auth.models import Group


# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    customer_profile_for_user_who_is_signed_in = Customer.objects.get(user_id=user.id)
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    print(customer_profile_for_user_who_is_signed_in)
    return render(request, 'customers/index.html')


# creating a new customer view function
def create(request):
    logged_in_customer = Customer.objects.get(user=request.user)
    context = {
        'logged_in_customer': logged_in_customer
    }
#    user = request.user
    if request.method == 'POST':
        # Get the current user who is signed
        # Grab the values from the inputs on the form
        # Create a new Customer object with all of the correct values
        # Call the .save() method on the new customer object
        # Redirect to the details page
        name = request.POST.get('name')
        weekly_pickup_day = request.POST.get('weekly_pickup_day')
        onetime_pickup = request.POST.get('onetime_pickup')
        start_suspension = request.POST.get('start_suspension')
        balance = request.POST.get('balance')
        zip_code = request.POST.get('zip_code')
        address = request.POST.get('address')
        new_customer = Customer(name=name,
                                weekly_pickup_day=weekly_pickup_day,
                                onetime_pickup=onetime_pickup,
                                start_suspension=start_suspension,
                                balance=balance,
                                zip_code=zip_code,
                                address=address)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html', context)

#        # Bring up the create.html file to the screen (this create.html file should have a form for creating a customer row)

# Edit customer view function


# def weekly(request):
#     return render(request, 'customers/weekly.html')
#
#
# def onetime(request):
#     return render(request, 'customers/onetime.html')
#
#
# def suspend(request):
#     return render(request, 'customers/suspend.html')
#
#
# def balance(request):
#     return render(request, 'customers/balance.html')


def details(request):
    logged_in_customer = Customer.objects.get(user=request.user)
    context = {
        'logged_in_customer': logged_in_customer
    }
    return render(request, 'customers/details.html', context)

from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    weekly_pickup_day = models.CharField(max_length=50)
    onetime_pickup = models.DateField(null=True)
    start_suspension = models.DateField(null=True)
    end_suspension = models.DateField(null=True)
    balance = models.IntegerField(default=0)
    zip_code = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


# add properties from slack message
# Andy does makemigrations again
# Andy does python manage.py migrate
# Andy does a add/commit/push to push migration files
# Corey and Sterling do add/commit/pull/push to get migration files
# OR Andy sends the migration files over slack
from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    # path('onetime/', views.onetime, name='onetime'),
    # path('suspend/', views.suspend, name='suspend'),
    # path('weekly/', views.weekly, name='weekly'),
    # path('balance/', views.balance, name='balance'),
    path('details/', views.details, name='details')
]
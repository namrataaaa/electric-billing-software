from django.contrib import admin
from django.urls import path, include
from . import views as billing_views

urlpatterns = [
    path('', billing_views.home, name='home'),
    path('make-payment/', billing_views.make_payment, name='make-payment'),
    path('bill-overview/', billing_views.bill_overview, name='bill-overview'),
    path('payment-report/', billing_views.payment_report, name='payment-report'),
    path('add-customer/', billing_views.add_customer, name='add-customer'),
]
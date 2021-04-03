from django.contrib import admin
from django.urls import path, include
from . import views as billing_views

urlpatterns = [
    path('', billing_views.home, name='home'),
    path('make-payment/', billing_views.make_payment, name='make-payment'),
    path('bill-overview/', billing_views.bill_overview, name='bill-overview'),
    path('payment-report/', billing_views.payment_report, name='payment-report'),
    path('add-customer/', billing_views.add_customer, name='add-customer'),
    path('ask-query/', billing_views.ask_query, name='ask-query'),
    path('generate-payment-report', billing_views.generate_payment_report, name='generate-payment-report'),
    path('generate-electricity-consumption', billing_views.generate_electricity_consumption, name='generate-electricity-consumption'),
    path('profile', billing_views.profile, name='profile'),
]
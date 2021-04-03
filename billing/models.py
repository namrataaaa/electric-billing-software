from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

class BillInformation(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    bill_number = models.CharField(max_length=8)
    amount_due = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(null=True)
    payment_status = models.BooleanField(default=False)

class Payment(models.Model):
    bill_info = models.ForeignKey(BillInformation, on_delete = models.CASCADE)
    transaction_id = models.CharField(max_length=10)
    payment_mode = models.CharField(max_length=20)
    card_number = models.IntegerField(null=True)
    account_number = models.IntegerField(null=True)





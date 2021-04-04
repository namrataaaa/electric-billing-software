from django.db import models
from django.contrib.auth.models import User



class Employee(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

class BillInformation(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    energy_units_consumed = models.FloatField(default=0)
    bill_number = models.CharField(max_length=8)
    amount_due = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(null=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.user.first_name

class Payment(models.Model):
    bill_info = models.ForeignKey(BillInformation, on_delete = models.CASCADE)
    transaction_id = models.CharField(max_length=10)
    payment_mode = models.CharField(max_length=20)
    card_number = models.IntegerField(null=True)
    account_number = models.IntegerField(null=True)

    def __str__(self):
        return self.bill_info.customer.user.first_name



def is_customer(self):
    try:
        curr_customer =  Customer.objects.get(user=self)
        if curr_customer.is_active:
            return True
        else:
            return False
    except:
        return False

def is_employee(self):
    try:
        curr_seller =  Employee.objects.get(user=self)
        return True
    except:
        return False

User.add_to_class("is_customer", is_customer)
User.add_to_class("is_employee", is_employee)
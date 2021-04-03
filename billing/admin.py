from django.contrib import admin
from .models import Employee, Customer, BillInformation, Payment


admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(BillInformation)
admin.site.register(Payment)
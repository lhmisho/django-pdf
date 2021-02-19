from django.contrib import admin
from .models import Customer, CustomerPdf
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerPdf)
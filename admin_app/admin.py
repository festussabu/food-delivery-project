from django.contrib import admin
from user_app.models import Customer
from vendor_app.models import * 
# Register your models here.

admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(FoodItem)
admin.site.register(Order)
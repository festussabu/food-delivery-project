from django.contrib import admin
from user_app.models import Customer, Order
from vendor_app.models import * 
from .models import Feedback, PnrGenerator, MoveTrain
# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Vendor)
admin.site.register(FoodItem)
admin.site.register(Feedback)
admin.site.register(PnrGenerator)
admin.site.register(MoveTrain)
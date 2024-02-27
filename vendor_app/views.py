from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vendor, FoodItem
from user_app.models import Order





# vendor registration
def vendor_registration_view(request):
  if request.method == 'POST':
    name = request.POST.get('vendor_name')
    email = request.POST.get('vendor_email')
    password = request.POST.get('vendor_password')
    if not name:
      messages.error(request, 'Name field is required')
      return redirect('vendor_app:vendor_reg')
    elif Vendor.objects.filter(vendor_name = name).exists():
      messages.error(request, 'This name already exits')
      return redirect('vendor_app:vendor_reg')
    elif Vendor.objects.filter(vendor_email = email).exists():
      messages.error(request, 'This email already exits')
      return redirect('vendor_app:vendor_reg')
    else:
      vendor_db = Vendor.objects.create(vendor_name = name, vendor_email=email, vendor_password=password)

      if vendor_db:
        return redirect('vendor_app:login_page')
  return render(request, 'vendor_registration.html')






#vendor home page
def vendor_home_page(request):
  food_items = FoodItem.objects.all()
  return render(request, 'vendor_page.html', {'food_items':food_items})





#delete product
def delete_product(request, id):
  food_items = FoodItem.objects.filter(id=id)
  food_items.delete()
  return redirect('vendor_app:vendor_page')





#update product
def update_food(request, id):
  food_items = FoodItem.objects.filter(id=id) 
  return render(request, 'update_food.html', {'update':food_items})


def updated_food(request):
  if request.method == 'POST':
    food_id = request.POST.get('food_item_id')
    food_name = request.POST.get('food_name')
    food_category = request.POST.get('food_category')
    food_price = request.POST.get('food_price')

    food_items = FoodItem.objects.filter(id=food_id).update(food_name=food_name, food_category=food_category, food_price=food_price)

    #for updating image field
    food_image = FoodItem.objects.get(id=food_id)
    food_image.food_image = request.FILES.get('food_image')
    food_image.save()
 
    return redirect('vendor_app:vendor_page')
  return render(request, 'update_food.html')





#vendor login
def login_page(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    if not email:
      messages.error(request, 'Enter your email')
      return redirect('vendor_app:login_page')
    if not password:
      messages.error(request, 'Enter your passwrod')
      return redirect('vendor_app:login_page')

      
      
    vendor_login = Vendor.objects.filter(vendor_email=email, vendor_password=password, vendor_approval_status=True)
    if vendor_login:
      return redirect('vendor_app:vendor_page')
    else:
      messages.error(request, 'Admin approval needed for login.. ')
  
  return render(request, 'login_page.html')





#add food
def add_food(request):
  if request.method == 'POST':
    food_name = request.POST.get('food_name')
    food_category = request.POST.get('food_category')
    food_price = request.POST.get('food_price')
    food_image = request.FILES.get('food_image')

    food_items = FoodItem.objects.create(food_name=food_name, food_category=food_category, food_price=food_price, food_image=food_image)
    
    if food_items:
      food_items.save()
      return redirect('vendor_app:vendor_page')
    else:
      messages.error(request, 'Something went wrong.')
      return redirect('vendor_app:add_food')
  return render(request, 'add_food.html')




#order page 
def order_page_vendor(request):

  order_items = Order.objects.all()
  return render(request, 'order_page_vendor.html', {'orders':order_items})
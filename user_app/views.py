from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer, Order
from vendor_app.models import FoodItem
from django.db.models import Q
from django.contrib.auth.decorators import login_required




#user Home page
def user_page(request):
    search_category = request.POST.get('search_category')
    if search_category:
      food_items = FoodItem.objects.filter(Q(food_category__iexact=search_category))
      if food_items:
        return render(request, 'user_page.html', {'food_items': food_items})
      else:
        return render(request, 'user_page.html',{'msg':'OOPS... NO ITEM FOUND'})

    food_items = FoodItem.objects.all()
    return render(request, 'user_page.html', {'food_items': food_items})



# user Registration
def user_registraion(request):

  if request.method == 'POST':
    user_name = request.POST.get('user_name')
    user_email = request.POST.get('user_email')
    user_password = request.POST.get('user_password')
    pnr_number = request.POST.get('pnr_number')
    train_number = request.POST.get('train_number')

    if not user_name:
      messages.error(request, 'Name field is required')
      return redirect('user_app:user_registration')
    elif Customer.objects.filter(username=user_name).exists():
      messages.error(request, 'Username already exitsts')
    elif Customer.objects.filter(email=user_email).exists():
      messages.error(request, 'Eamil already exitsts')

    else:
      user_db = Customer.objects.create(username=user_name, email=user_email, password=user_password, pnr_number=pnr_number, train_number=train_number)

      if user_db:
        return redirect('user_app:user_page')

  return render(request, 'user_registration.html')





#customer login
def login_page_user(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    if not email:
      messages.error(request, 'Email field is required')
      return redirect('user_app:login_page_user')
    
    user_login = Customer.objects.filter(email=email, password=password)
    if user_login:


      for logged_in_user in user_login:  
        
        train_number = logged_in_user.train_number
        request.session['train_number']=train_number

        current_user = logged_in_user.username
        request.session['current_user']=current_user

        
        
      return redirect('user_app:user_page')
    else:
      messages.error(request, 'Invalid login.')
  
  return render(request, 'login_page.html')





#remove order items
def order_page_remove_item(request, id):
  order_db = Order.objects.filter(id=id)
  order_db.delete()
  return redirect('user_app:order_page')





#order page
def order_page(request):
  if request.method == 'POST':
    food_name = request.POST.get('food_name')
    food_price = request.POST.get('food_price')

    order_db= Order.objects.create(customer_name=request.session['current_user'], train_number=request.session['train_number'],  product_name=food_name, price=food_price)    
    return redirect('user_app:order_page')

  order_db = Order.objects.all()
  return render(request, 'order_page.html', {'orders':order_db})



#feedback by user page
def feedback_by_user(request):
  return render(request, 'feedback_by_user_page.html')
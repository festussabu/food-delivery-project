from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer

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

#user Home page
def user_page(request):
  return render(request, 'user_page.html')

#login
def login_page_user(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    if not email:
      messages.error(request, 'Email field is required')
      return redirect('user_app:login_page_user')
    
    user_login = Customer.objects.filter(email=email, password=password)
    if user_login:
      return redirect('user_app:user_page')
    else:
      messages.error(request, 'Invalid login.')
  
  return render(request, 'login_page.html')
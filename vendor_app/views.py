from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Vendor

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
      messages.success(request, 'Registration successful. You can now log in.')

      if vendor_db:
        return redirect('vendor_app:vendor_page')
  return render(request, 'vendor_registration.html')

#vendor home page
@login_required()
def vendor_home_page(request):
  return render(request, 'vendor_page.html')

#login
def login_page(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    if not email:
      messages.error(request, 'Enter your email')
      return redirect('vendor_app:login_page')
    vendor_login = Vendor.objects.filter(vendor_email=email, vendor_password=password)
    if vendor_login:
      return redirect('vendor_app:vendor_page')
    else:
      messages.error(request, 'Email or Password is incorrect.')
  
  
  return render(request, 'login_page.html')
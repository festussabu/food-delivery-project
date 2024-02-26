from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SuperuserLoginForm
from django.contrib.auth.decorators import login_required
from vendor_app.models import Vendor







#index page
def index_page(request):
    return render(request, 'index_page.html')

@login_required(login_url='superuser_login')
def admin_page(request):
    return render(request, 'admin_page.html')

def superuser_login(request):
    if request.method == 'POST':
        form = SuperuserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin_app:admin_page')  
            else:
                return render(request, 'superuser_login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = SuperuserLoginForm()
    return render(request, 'superuser_login.html', {'form': form})






#rendering vendor objects
def vendor_details(request):
    vendor_object = Vendor.objects.all()
    return render(request, 'admin_watch_vendors.html', {'vendor_object':vendor_object})






#remove vendor by admin
def remove_vendor(request, id):
    vendor_object = Vendor.objects.filter(id =id)
    vendor_object.delete()
    return redirect('admin_app:vendor_details')





#approve vendor by admin
def approve_vendor(request):
    if request.method == 'POST':
        vendor_id = request.POST.get('idno')
        approval_status=Vendor.objects.get(id=vendor_id)
        approval_status.vendor_approval_status=True
        if approval_status:
            approval_status.save()
            return redirect('admin_app:approve_vendor')

    vendor_object = Vendor.objects.all()
    return render(request, 'admin_approve_vendor.html',{'vendor_object':vendor_object})


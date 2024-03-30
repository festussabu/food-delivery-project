from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SuperuserLoginForm
from django.contrib.auth.decorators import login_required
from vendor_app.models import Vendor, FoodItem
from user_app.models import Order, Customer
from .models import Feedback, MoveTrain
from django.http import Http404



#this will prevent from user directly accessing urls
def get_referer(request):
  referer = request.META.get('HTTP_REFERER')
  if not referer:
     return None
  return referer


#index page
def index_page(request):
    return render(request, 'index_page.html')


def admin_page(request):
    #this should be used in the page where you don't need the user to have direct url access 
    if not get_referer(request):
        raise Http404
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
    if not get_referer(request):
        raise Http404
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



#order page 
def order_page_admin(request):
  order_items = Order.objects.all()
  return render(request, 'order_page_admin.html', {'orders':order_items})




#rendering user objects
def user_details(request):
    customers = Customer.objects.all()
    return render(request, 'admin_watch_users.html', {'customers':customers})


#remove user by admin
def remove_user(request, id):
    filtered_users = Customer.objects.filter(id=id)
    filtered_users.delete()
    return redirect('admin_app:user_details')




#feedback page
def feedback_page(request):
    
  #this will remove duplicates.
#   feedback_db = Order.objects.values_list('customer_name',flat=True).distinct()
  feedback_db = Feedback.objects.all()
#   date = Order.objects.values_list('date', flat=True).distinct()
  return render(request, 'feedback_page.html', {'feedback_db':feedback_db})



#rendering food products
def admin_food_items(request):
    food_items = FoodItem.objects.all()
    return render(request, 'admin_food_items.html', {'food_items':food_items})



def move_train(request):

    if request.method == 'POST':
        selected_station = request.POST.get('station_name')
        try:
            station = MoveTrain.objects.get(id=4)
            station.current_station = selected_station
            station.save()
        except MoveTrain.DoesNotExist:
            # Handle the case where the object with id=1 doesn't exist
            print("lier.")

    return render(request, 'move_train.html')
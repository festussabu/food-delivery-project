from django.urls import path
from .views import superuser_login, admin_page, index_page, vendor_details, remove_vendor, approve_vendor, order_page_admin, user_details, remove_user, feedback_page, admin_food_items

app_name = 'admin_app'

urlpatterns = [
    path('', index_page, name='index_page'),
    path('superuser/login/', superuser_login, name='superuser_login'),
    path('admin_page/', admin_page, name='admin_page'),
    path('vendor_details/', vendor_details, name='vendor_details'),
    path('remove_vendor/<int:id>', remove_vendor, name='remove_vendor'),
    path('approve_vendor/', approve_vendor, name='approve_vendor'),
    path('order_page_admin/', order_page_admin, name='order_page_admin'),
    path('user_details/', user_details, name='user_details'),
    path('remove_user/<int:id>/', remove_user, name='remove_user'),
    path('feedback_page/', feedback_page, name='feedback_page'),
    path('admin_food_items/', admin_food_items, name='admin_food_items'),
    
]
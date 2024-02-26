from django.urls import path
from .views import superuser_login, admin_page, index_page, vendor_details, remove_vendor, approve_vendor

app_name = 'admin_app'

urlpatterns = [
    path('', index_page),
    path('superuser/login/', superuser_login, name='superuser_login'),
    path('admin_page/', admin_page, name='admin_page'),
    path('vendor_details/', vendor_details, name='vendor_details'),
    path('remove_vendor/<int:id>', remove_vendor, name='remove_vendor'),
    path('approve_vendor/', approve_vendor, name='approve_vendor')
]
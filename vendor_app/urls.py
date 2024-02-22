from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'vendor_app'

urlpatterns = [
    path('vendor_reg/', views.vendor_registration_view, name='vendor_reg'),
    path('vendor_page/', views.vendor_home_page, name='vendor_page'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('login_page/', views.login_page, name='login_page'),
    path('add_food/', views.add_food, name='add_food'),
    path('update_food/<int:id>', views.update_food, name='update_food'),
    path('updated_food/', views.updated_food, name='updated_food'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'vendor_app'

urlpatterns = [
    path('vendor_reg/', views.vendor_registration_view, name='vendor_reg'),
    path('vendor_page', views.vendor_home_page, name='vendor_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('add_food/', views.add_food, name='add_food'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
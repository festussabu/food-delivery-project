from django.urls import path
from . import views

app_name = 'vendor_app'

urlpatterns = [
    path('vendor_reg/', views.vendor_registration_view, name='vendor_reg'),
    path('vendor_page', views.vendor_home_page, name='vendor_page'),
    path('login_page/', views.login_page, name='login_page'),
]
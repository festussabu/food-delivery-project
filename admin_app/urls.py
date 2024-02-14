from django.urls import path
from .views import superuser_login, admin_page

app_name = 'admin_app'

urlpatterns = [
    path('superuser/login/', superuser_login, name='superuser_login'),
    path('admin_page/', admin_page, name='admin_page')
]
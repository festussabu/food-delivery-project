from django.urls import path
from .views import user_registraion, user_page, login_page_user
app_name = 'user_app'

urlpatterns = [
    path('user_registration/', user_registraion, name='user_registration'),
    path('user_page/', user_page, name='user_page'),
    path('login_page_user/', login_page_user, name='login_page_user'),
]
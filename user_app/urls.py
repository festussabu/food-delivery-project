from django.urls import path
from .views import user_registraion, user_page, login_page_user, order_page, order_page_remove_item
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user_app'

urlpatterns = [
    path('user_registration/', user_registraion, name='user_registration'),
    path('user_page/', user_page, name='user_page'),
    path('login_page_user/', login_page_user, name='login_page_user'),
    path('order_page/', order_page, name='order_page'),
    path('order_page_remove_item/<int:id>', order_page_remove_item, name='order_page_remove_item'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
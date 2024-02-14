from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SuperuserLoginForm


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
                # Redirect to the admin page or any other page you want
                return redirect('admin_app:admin_page')  
            else:
                return render(request, 'superuser_login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = SuperuserLoginForm()
    return render(request, 'superuser_login.html', {'form': form})
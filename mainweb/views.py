from django.shortcuts import render, redirect
from mainweb.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('show_post')
    else:
        return redirect('show_post')

def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Acerca de'
    })


def login_page(request):
    if request.user.is_authenticated:
        return redirect('show_post')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('show_post')
            else:
                messages.error(
                    request, 'El usuario o la contraseña son incorrectos')

    return render(request, 'user/login.html', {
        'title': 'Login'
    })


def logout_user(request):
    logout(request)
    return redirect('login')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('show_post')
    else:
        register_form = RegisterForm()
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                # Mostrar un mensaje flash que se muestra una sola vez
                messages.success(request, 'Te has registrado correctamente!!')
                return redirect('login')

    return render(request, 'user/register.html', {
        'title': 'Register',
        'register_form': register_form
    })

from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views import View
from django.shortcuts import render, redirect

from users.forms import LoginForm


class LoginView(View):

    def get(self, request):
        context = {'form': LoginForm()}
        return render(request, "login_form.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("login_username")
            password = form.cleaned_data.get("login_password")
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user and authenticated_user.is_active:
                django_login(request, authenticated_user)
                return redirect('home_page')
            else:
                # messages.error(request, "Usuario incorrecto o inactivo")
                form.add_error(None, "Usuario incorrecto o inactivo")
        return render(request, "login_form.html", {'form': form})


def logout(request):
    django_logout(request)
    return redirect('login_page')

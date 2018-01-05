from django import forms


class LoginForm(forms.Form):

    login_username = forms.CharField(label="Nombre de usuario")
    login_password = forms.CharField(label="Contraseña")

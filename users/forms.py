from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

from django import forms
from django.contrib.auth import authenticate
from django.utils.text import capfirst

class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField(label=capfirst('Email'), widget=forms.EmailInput(attrs={"autofocus": True}))
    password = forms.CharField(label='Parol', strip=False, widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user = authenticate(username=email, password=password)  # ← emailni username sifatida jo'natyapmiz
            if self.user is None:
                raise forms.ValidationError("Email yoki parol noto‘g‘ri.")
        return self.cleaned_data

    def get_user(self):
        return self.user


class CustomProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'profile_image']


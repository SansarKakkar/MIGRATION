from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Registration form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'full_name', 'username', 'password1', 'password2']

# # Login form (Optional - if customizing login with email explicitly)
# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.EmailField(label='Email')  # Override username with email


class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                raise forms.ValidationError("Invalid email or password.")
        return self.cleaned_data

    def get_user(self):
        return self.user

from django import forms
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ServiceProvider
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)



class SPLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class AddServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['username', 'password']

class DeleteServiceProviderForm(forms.Form):
    delete_provider = forms.ModelChoiceField(
        queryset=ServiceProvider.objects.all(),
        label="Select a service provider to delete",
        required=False,
        empty_label="---------",
        to_field_name="username"
        )


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['event_type', 'name', 'email']

# forms.py


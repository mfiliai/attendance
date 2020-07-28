from django.forms import ModelForm
from .models import Staff
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.contrib.auth.models import User
class StaffForm(ModelForm):
	class Meta:
		model = Staff
		fields = '__all__'
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields=['username', 'email', 'password1', 'password2']
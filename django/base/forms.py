
from . models import Student
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

# to create model form 
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # to apply css 
        widgets = {
                'name' : forms.TextInput(attrs={'class':'my-name', 'placeholder':'Enter your name'}),
                'email' : forms.EmailInput(attrs={'class':'my-email', 'placeholder':'Enter your email'}),
                'std' : forms.TextInput(attrs={'class':'my-std', 'placeholder':'Enter your std'})}


# to create custom form for signup using UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class CustomUserChangeForm(UserChangeForm):
    password = None # to avoid display password on page
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email' : 'Email'} # to update label in form. here we are updating for email 
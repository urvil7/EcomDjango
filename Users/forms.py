from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Contact
from django.contrib.auth.forms import PasswordResetForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = _("There is no user registered with the specified E-Mail address.")
            self.add_error('email', msg)
        return email

class ContactAddForm(forms.ModelForm):
    Name = forms.CharField(max_length=50)
    Email = forms.EmailField()
    Subject = forms.CharField(max_length=50)
    Message = forms.Textarea()

    class Meta:
        model = Contact
        fields = ['Name','Email','Subject','Message'] 
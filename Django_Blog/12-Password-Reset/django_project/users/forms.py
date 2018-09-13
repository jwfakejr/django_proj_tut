from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        users = User.objects.all().values()
        dup_email = False
        for user in users:
            print(user)
            if 'email' in user:

                if user['email'] == self.cleaned_data.get('email'):
                    print('found duplicate email')
                    dup_email = True
        if dup_email is True:
            raise forms.ValidationError('email is already being used!')
        else:
            return self.cleaned_data.get('email')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

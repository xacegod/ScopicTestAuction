from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserBalance, UserBiddingSetting


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserBalance.objects.get_or_create(user=user, amount=100) # on creation adds balance of 100
            UserBiddingSetting.objects.get_or_create(user=user) # on user creation creates and sets auto bid to false
        return user

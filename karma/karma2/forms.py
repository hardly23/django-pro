from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class userProfileInfo(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields =  ('name_id','mobile','address','alternate_mobil_number',
                   'Address_line1','Address_line2','City','State','Zipcode','Country')



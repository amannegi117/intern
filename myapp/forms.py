from .models import *
from django import forms
class uploadform(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo' : ''}

class create_profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['foto','bio']
        labels = {'foto': ''}

class create_user(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email']

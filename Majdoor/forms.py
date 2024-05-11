# users/forms.py
from django import forms
from .models import Majdoor_db, Users_db

class Majdoor_signup_form(forms.ModelForm):
    class Meta:
        model = Majdoor_db
        fields = '__all__'

class Customer_signup_form(forms.ModelForm):
    class  Meta:
        model = Users_db
        fields = '__all__'
        


class Majdoor_login(forms.Form):
    m_id = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    
class Customer_login(forms.Form):
    c_id = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
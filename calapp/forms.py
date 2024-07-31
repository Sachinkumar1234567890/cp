from django import forms
from .models import *



class newfoodform(forms.ModelForm):
    class Meta:
        model=foodModel
        fields=['name','type','quantity','protein','carbs','fat','nutrients','vitamins','foodimg']

class editfoodform(forms.ModelForm):
    class Meta:
        model=dailycalory
        fields=['dname','dtype','dquantity','dprotein','dcarbs','dfat','dnutrients','dvitamins']

class register_form(forms.ModelForm):
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    class Meta:
        model=user_register
        fields=['name','phone','email','password','confirm_password']




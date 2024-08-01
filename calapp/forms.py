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






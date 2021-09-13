from django import forms
from django.db.models.base import Model
from django import forms
from django.forms import ModelForm, Select
from .models import DropDown


class DropDownForm(ModelForm):
    class Meta:
        model = DropDown
        fields = ['data_drop']
    
        widgets = {'data_drop': Select(attrs= {'class':'form-select'})}
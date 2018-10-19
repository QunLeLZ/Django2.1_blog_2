from django import forms
from .models import Gbook

class GbookForm(forms.ModelForm):
    class Meta:
        model = Gbook
        fields = ['name','email','text']
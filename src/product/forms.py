from django import forms
from .models import Debtors


class DebetorsForm(forms.ModelForm):
    class Meta:
        model = Debtors
        fields = ['full_name', 'phone_numuber', 'product', 'date', 'price'] 
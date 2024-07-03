from django import forms
from .models import Product, About

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {'name', 'price', 'cotegory', 'image'}

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['f_name', 'l_name', 'place']
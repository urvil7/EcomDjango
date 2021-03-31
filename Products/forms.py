from django import forms
from .models import Order
from django import forms

class ProductAddForm(forms.Form):
    Name = forms.CharField(label='your name',max_length=50)
    Price = forms.DecimalField(max_digits=8,decimal_places=2)
    Size = forms.CharField(max_length=10)
    Color = forms.CharField(max_length=20)
    Quantity = forms.CharField(max_length=10)
    class Meta:
        model = Order
        fields = [ 'Name','Price', 'Color', 'Size' , 'Quantity']
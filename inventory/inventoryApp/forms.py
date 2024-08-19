from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Product Name',
            'sku': 'SKU',
            'price': 'Price',
            'supplier': 'Supplier',
            'quantity': 'Quantity',
        }
        widgets = {
            'product_id': forms.NumberInput(attrs={
                'placeholder': 'e.g 1', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g 1', 'shirt': 'form-control'}),
            'sku': forms.TextInput(attrs={
                'placeholder': 'e.g D12345', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={
                'placeholder': 'e.g 19.99', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={
                'placeholder': 'e.g 10', 'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={
                'placeholder': 'e.g Some Company', 'class': 'form-control'}),
        }

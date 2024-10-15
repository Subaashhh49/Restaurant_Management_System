from django import forms
from .models import Category, Menu, Table, Waiter, Order, Reception

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'price', 'category']

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['table_number', 'capacity']

class WaiterForm(forms.ModelForm):
    class Meta:
        model = Waiter
        fields = ['name', 'contact_number']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table', 'waiter', 'menu',  'quantity']


class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ['name', 'contact_number', 'email']

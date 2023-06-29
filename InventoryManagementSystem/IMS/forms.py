from django import forms
from .models import Inventory, Order, Transaction


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name',
            'quantity',
            'cost'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control'})


class TransactionItemForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'name',
            'quantity',
            'selling_price'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['selling_price'].widget.attrs.update({'class': 'form-control'})


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = [
            'name',
            'cost',
            'quantity',
            'quantity_sold',
            'selling_price',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity_sold'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['selling_price'].widget.attrs.update(
            {'class': 'form-control'})

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = [
            'name',
            'iin',
            'cost',
            'quantity',
            'selling_price',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['iin'].widget.attrs.update({'class': 'form-control'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['selling_price'].widget.attrs.update(
            {'class': 'form-control'})

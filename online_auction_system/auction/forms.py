
from django import forms
from .models import AuctionItem

class AuctionItemForm(forms.ModelForm):
    class Meta:
        model = AuctionItem
        fields = '__all__'
        
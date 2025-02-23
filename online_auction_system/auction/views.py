
from django.shortcuts import render, redirect
from .models import AuctionItem
from .forms import AuctionItemForm

# Home page view
def home(request):
    items = AuctionItem.objects.all()
    return render(request, 'home.html', {'items': items})

# Item detail view
def auction_item(request, item_id):
    item = AuctionItem.objects.get(pk=item_id)
    return render(request, 'auction_item.html', {'item': item})

# Add item view
def add_item(request):
    if request.method == 'POST':
        form = AuctionItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuctionItemForm()
    return render(request, 'add_item.html', {'form': form})
        
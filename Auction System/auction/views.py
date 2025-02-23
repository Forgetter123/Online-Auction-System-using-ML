from django.shortcuts import render
def auction_list(request):
    return render(request, 'auction/auction_list.html')
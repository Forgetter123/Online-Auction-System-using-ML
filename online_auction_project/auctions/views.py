
from django.shortcuts import render, get_object_or_404
from .models import Auction
from ml.price_prediction import predict_price
from ml.recommendation import recommend_items

def auction_list(request):
    auctions = Auction.objects.all()
    return render(request, 'auctions/index.html', {'auctions': auctions})

def auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)
    predicted_price = predict_price(auction)
    return render(request, 'auctions/auction_detail.html', {
        'auction': auction,
        'predicted_price': predicted_price
    })

def recommendations(request):
    user_preferences = request.GET.get('preferences', 'all')
    recommended_items = recommend_items(user_preferences)
    return render(request, 'auctions/recommendations.html', {'recommendations': recommended_items})

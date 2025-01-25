
from auctions.models import Auction

def recommend_items(category):
    recommendations = Auction.objects.filter(category=category).order_by('-seller_rating')[:5]
    return recommendations


from django.db import models

class Auction(models.Model):
    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    item_condition = models.IntegerField()
    starting_price = models.FloatField()
    final_price = models.FloatField(null=True, blank=True)
    bids_count = models.IntegerField()
    auction_duration = models.IntegerField()
    seller_rating = models.FloatField()
    buyer_region = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name

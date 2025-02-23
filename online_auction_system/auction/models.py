
from django.db import models

class AuctionItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    item_condition = models.CharField(max_length=100)
    starting_price = models.FloatField()
    final_price = models.FloatField(null=True, blank=True)
    bids_count = models.IntegerField(default=0)
    auction_duration = models.IntegerField()  # In hours
    seller_rating = models.FloatField()
    buyer_region = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name
        
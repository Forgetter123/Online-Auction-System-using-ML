from django.db import models
class AuctionItem(models.Model):
    item_name = models.CharField(max_length=255)
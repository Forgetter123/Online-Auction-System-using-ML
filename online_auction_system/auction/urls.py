
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<int:item_id>/', views.auction_item, name='auction_item'),
    path('add/', views.add_item, name='add_item'),
]
        

from django.urls import path
from . import views

urlpatterns = [
    path('', views.auction_list, name='auction_list'),
    path('auction/<int:auction_id>/', views.auction_detail, name='auction_detail'),
    path('recommendations/', views.recommendations, name='recommendations'),
]

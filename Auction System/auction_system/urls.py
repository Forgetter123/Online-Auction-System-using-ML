from django.urls import path, include
urlpatterns = [path('auction/', include('auction.urls'))]
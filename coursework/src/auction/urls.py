from django.urls import path
from . import views

urlpatterns = [
    path('bid/add/', views.createBid),
    path('auction/add/', views.createAuction),
    path('itemBids/<int:itemId>', views.itemBids), 
]


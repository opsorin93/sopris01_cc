from django.shortcuts import render
from django.http import HttpResponse
import json
from datetime import datetime
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import AuctionItem, Bid
from .serializers import AuctionItemSerializer, BidSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.decorators import login_required


class AuctionItemViewSet(viewsets.ModelViewSet):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemSerializer

class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

@api_view(['POST'])
@login_required
def createBid(request):
    bid = BidSerializer(data=request.data)
    if bid.is_valid():
        if bidAllowed(request):
                bid.save()
                return Response(bid.data)
        else:
            return Response({'detail': 'User can not bid on thier own auction'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(bid.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@login_required
def createAuction(request):
    auctionItem = AuctionItemSerializer(data=request.data)
    if auctionItem.is_valid():
        auctionInDB = auctionItem.save()
        return Response(auctionItem.data)
    return Response(auctionItem.errors, status=status.HTTP_400_BAD_REQUEST)

def bidAllowed(request):
    bid = BidSerializer(data=request.data)
    if bid.is_valid():
        auctionItemId = bid.data['item']
        bidAuction = AuctionItem.objects.get(pk=auctionItemId)
        auctionUser = bidAuction.created_by_id
        bidUser = request.user.id
        return auctionUser != bidUser
    return False
    
def itemBids(request, itemId):
    a = AuctionItem(id=itemId)
    all = Bid.objects.all()
    myItem = Bid(item=a)
    some = Bid.objects.all().filter(item=a)
    serializer = BidSerializer(some, many=True)
    json = JSONRenderer().render(serializer.data)
    html = "<html><body>Item bids: %s.</body></html>" % json
    return HttpResponse(html)

 

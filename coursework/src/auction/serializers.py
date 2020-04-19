from rest_framework import serializers
from .models import AuctionItem
from .models import Bid

class AuctionItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuctionItem
        fields = ('id', 'title', 'condition', 'description', 'price', 'endDate', 'ended', 'winner','created_by')


class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = ('id', 'amount', 'time', 'item','created_by')


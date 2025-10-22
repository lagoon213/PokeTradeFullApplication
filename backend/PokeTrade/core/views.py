from django.shortcuts import render
from rest_framework.views import APIView
from .models import Card
from .serializer import *
from rest_framework.response import Response

# Create your views here.
class CardView(APIView):
    serializer_class = CardSerializer

    def get(self, request):
        cards = [{'name': card.name, 'description': card.description,'price': card.price, 'set_name': card.set_name, 'number': card.number, 'rarity': card.rarity, 'image_url': card.image_url} for card in Card.objects.all()]
        return Response(cards)

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
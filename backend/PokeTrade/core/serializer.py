from rest_framework import serializers
from .models import *

#vertaals de python modellen naar JSON bestanden
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
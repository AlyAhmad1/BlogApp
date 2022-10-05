from rest_framework import serializers
from .models import ItemList


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = ['id', 'title', 'description', 'quantity']

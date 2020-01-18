from .models import Item
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'imgUrl', 'name', 'price', 'ingredients', 'monthlySales']

class ItemSerializerWithId(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'imgUrl', 'name', 'price', 'gender', 'category', 'ingredients', 'monthlySales']

class ItemSerializerThumbnail(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'imgUrl', 'name', 'price']
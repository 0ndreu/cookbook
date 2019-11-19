from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class UserSerializer(serializers.Serializer):
    """"
    Сериализация пользователя
    """
    class Meta:
        model = User
        fields = ('id', 'username')


class ProductSerializer(serializers.Serializer):
    """
    Сериализация продуктов
    """
    class Meta:
        model = Product
        fields = ('title', 'description', 'metric', 'calories', 'proteins', 'fats', 'carbohydrates')


class TimeToEatSerializer(serializers.Serializer):

    class Meta:
        model = TimeToEat
        fields = 'time_to_eat'      # is that true??


class ReceiptSerializer(serializers.Serializer):
    """
    Сериализация рецептов
    """
    creator = UserSerializer()
    time_to_eat = TimeToEatSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Receipt
        fields = ('title', 'creator', 'description', 'time_to_eat', 'date', 'products', 'calories',
                  'proteins', 'fats', 'carbohydrates', 'moderation')


class FridgeSerializer(serializers.Serializer):
    """"
    Сериализация холодильника
    """
    user = UserSerializer()
    product = ProductSerializer()

    class Meta:
        model = Fridge
        fields = ('user', 'product', 'how_many')

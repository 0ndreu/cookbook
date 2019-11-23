from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    """"
    Сериализация пользователя
    """
    class Meta:
        model = User
        fields = ('id', 'username')


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализация продуктов
    """
    class Meta:
        model = Product
        fields = ('title', 'description', 'metric', 'calories', 'proteins', 'fats', 'carbohydrates')


class TimeToEatSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeToEat
        fields = 'time_to_eat'      # is that true??


class ReceiptSerializer(serializers.ModelSerializer):
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


class ProductForFridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'metric')


class FridgeSerializer(serializers.ModelSerializer):
    """"
    Сериализация холодильника
    """
    product = ProductForFridgeSerializer()

    class Meta:
        model = Fridge
        fields = ('product', 'how_many')

# class FridgePostSerializer
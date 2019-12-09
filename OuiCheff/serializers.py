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


class ProductForFridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'metric')


class ReceiptSerializer(serializers.ModelSerializer):
    """
    Сериализация рецептов
    """
    # creator = UserSerializer()
    # time_to_eat = TimeToEatSerializer(many=False)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # products = ProductSerializer(many=True)
    # product = PrimaryKeyRelatedField(required=True,
    #                                  queryset=Product.objects.all())

    class Meta:
        model = Receipt
        fields = ('title', 'description', 'date', 'calories',
                  'proteins', 'fats', 'carbohydrates', 'time_to_eat', 'creator')
        # fields = '__all__'


class FridgeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    how_many = serializers.IntegerField(required=True,
                                        min_value=0)
    product = serializers.PrimaryKeyRelatedField(required=True,
                                                 queryset=Product.objects.all())

    class Meta:
        model = Fridge
        fields = '__all__'


class ProductsInReceiptSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(required=True,
                                                 queryset=Product.objects.all())
    receipt = serializers.PrimaryKeyRelatedField(required=True,
                                                 queryset=Receipt.objects.all())
    # receipt = serializers.PrimaryKeyRelatedField(default=serializers.)
    count_of_product = serializers.IntegerField(required=True,
                                                min_value=0)

    class Meta:
        model = ReceiptHasProduct
        fields = '__all__'

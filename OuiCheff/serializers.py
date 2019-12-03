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
    # time_to_eat = TimeToEatSerializer(many=False)
    products = ProductSerializer(many=True)

    class Meta:
        model = Receipt
        fields = ('title', 'creator', 'description', 'date', 'products', 'calories',
                  'proteins', 'fats', 'carbohydrates', 'moderation')
        # fields = '__all__'


class ProductForFridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'metric')


class FridgeDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)

    class Meta:
        model = Fridge
        fields = '__all__'


class FridgeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    how_many = serializers.IntegerField(required=True,
                                        min_value=0)
    product = serializers.PrimaryKeyRelatedField(required=True,
                                                 queryset=Product.objects.all())

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     how_many = validated_data['nums']
    #     product = validated_data['product']
    #
    #     existed = Fridge.objects.filter(user=user, product=product)
    #
    #     if existed:
    #         existed = existed[0]
    #         existed.nums += how_many
    #         existed.save()
    #     # 如果购物车车没有记录，就创建
    #     else:
    #         existed = Fridge.objects.create(**validated_data)
    #
    #     return existed

    # def update(self, instance, validated_data):
    #     instance.how_many = validated_data['how_many']
    #     instance.save()
    #     return instance

    class Meta:
        model = Fridge
        fields = '__all__'

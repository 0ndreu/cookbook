from rest_framework.views import APIView        # с помоцью него классы рест фрейверка
from rest_framework.response import Response    # вывод ответа на клиентскую часть
from rest_framework import permissions, viewsets, status, generics       # проверять пользователя и давать доступы
from django.shortcuts import get_object_or_404

from .serializers import *


class ProductViewSet(viewsets.ModelViewSet):
    """
    Выводит список продуктов и добавляет новый продукт
    """
    permission_classes = [permissions.IsAuthenticated, ]

    serializer_class = ProductSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Product.objects.all()


class FridgeViewSet(viewsets.ModelViewSet):
    """
    продукты в холодильнике и их добавление
    """
    serializer_class = FridgeSerializer

    def get_queryset(self):
        return Fridge.objects.filter(user=self.request.user)


class ReceiptsViewSet(viewsets.ModelViewSet):
    permissions = [permissions.IsAuthenticated]

    serializer_class = ReceiptSerializer
    lookup_field = 'id'

    queryset = Receipt.objects.filter(moderation=True)


class ReceiptHasProductView(viewsets.ModelViewSet):
    """
    во вью:                                                     ?????????????????
    url: 'http://127.0.0.1:8000/products_in_receipt/',
    type: 'GET',
    data: {
        receipt: this.id,
    },                                                          ?????????????????
    """
    serializer_class = ProductsInReceiptSerializer
    # TODO нельзя добавлять продукт, который уже есть в рецепте

    def get_queryset(self):
        receipt = self.request.GET.get('receipt')
        return ReceiptHasProduct.objects.filter(receipt_id=receipt)


class GiveDishView(viewsets.ViewSet):
    # TODO совместить с холодильником
    """
        Берём все продукты в холодильнике
        Сравниваем со всеми рецептами
        Если есть рецепт, в котором все продукты:
        Выводим
        Если нет:
        Берём все продукты - 1

        Если нет продуктов в холодильнике: рандомный рецепт
    """
    def list(self, request):
        time_to_eat = request.GET.get('time_to_eat')
        calories = request.GET.get('calories')
        cal_low = int(calories) * 0.9
        cal_high = int(calories) * 1.1
        queryset = Receipt.objects.filter(time_to_eat=time_to_eat).filter(calories__gt=str(int(cal_low)))
        queryset.filter(calories__lt=str(int(cal_high))).order_by('?')[:1]

        eat = get_object_or_404(queryset)
        serializer = ReceiptSerializer(eat)
        return Response(serializer.data)


def take_calories(calories):
    cal_low = int(calories) * 0.9
    cal_high = int(calories) * 1.1
    return str(int(cal_high)), str(int(cal_low))


def get_all_products_in_fridge(self):
    queryset = Fridge.objects.filter(user=self.request.user)
    serializer = FridgeSerializer(queryset)
    return serializer.data


class DishFromFridge(viewsets.ViewSet):
    """
        Берём все продукты в холодильнике
        Сравниваем со всеми рецептами
        Если есть рецепт, в котором все продукты:
        Выводим
        Если нет:
        Берём все продукты - 1

        Если нет продуктов в холодильнике: рандомный рецепт
    """

    # def list(self, request):
    #     calories = request.GET.get('calories')
    #     user = self.request.user
    #     if Fridge.objects.filter(user=user) is None:
    #         queryset = Receipt.objects.order_by('?')[:-1]
    #         rand_receipt = get_object_or_404(queryset)
    #         serializer = ReceiptSerializer(rand_receipt)
    #         return Response(serializer.data)
    #     else:
    #         cal_high, cal_low = take_calories(calories)
    #         fridge_serializer = get_all_products_in_fridge(self)
    #
    #         for product in fridge_serializer.product_id:
    #             pass
    def list(self, request):

        def get_dish_generator():
            queryset_receipt_has_product = ReceiptHasProduct.objects.distinct('receipt')
            queryset_fridge = Fridge.objects.filter(user=request.user)
            fridge = FridgeSerializer(queryset_fridge)
            receipts = ProductsInReceiptSerializer(queryset_receipt_has_product)
            necessary_rep = {}
            max_match = 0
            for receipt in receipts:
                match = 0
                for product in fridge:
                    if product in receipt:
                        match += 1
                if match > max_match:
                    necessary_rep = receipt
            return necessary_rep







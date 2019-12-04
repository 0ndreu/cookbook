from rest_framework.views import APIView        # с помоцью него классы рест фрейверка
from rest_framework.response import Response    # вывод ответа на клиентскую часть
from rest_framework import permissions, viewsets, status, generics       # проверять пользователя и давать доступы
from rest_framework.decorators import action

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

    queryset = Receipt.objects.all()


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

    def get_queryset(self):
        receipt = self.request.GET.get('receipt')
        return ReceiptHasProduct.objects.filter(receipt=receipt)

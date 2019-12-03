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
    permissions = [permissions.AllowAny]

    serializer_class = ReceiptSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Receipt.objects.all()

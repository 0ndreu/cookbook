from rest_framework.views import APIView        # с помоцью него классы рест фрейверка
from rest_framework.response import Response    # вывод ответа на клиентскую часть
from rest_framework import permissions, viewsets, status, generics       # проверять пользователя и давать доступы
from rest_framework.decorators import action

from .serializers import *


class Products(APIView):
    """
    Выводит список продуктов и добавляет новый продукт
    """
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class FridgeViewSet(viewsets.ModelViewSet):
    """
    продукты в холодильнике и их добавление
    """
    serializer_class = FridgeSerializer
    lookup_field = 'product_id'

    def get_queryset(self):
        return Fridge.objects.filter(user=self.request.user)

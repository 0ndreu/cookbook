from rest_framework.views import APIView        # с помоцью него классы рест фрейверка
from rest_framework.response import Response    # вывод ответа на клиентскую часть
from rest_framework import permissions, status, generics       # проверять пользователя и давать доступы

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

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Fridges(APIView):
    """
    Холодильник
    """
    permission_classes = [permissions.AllowAny ]

    def get(self, request):
        fridges = Fridge.objects.filter(user=request.user)
        serializer = FridgeSerializer(fridges, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        pass



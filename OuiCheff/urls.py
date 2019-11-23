from django.urls import path, include
from .views import *

urlpatterns = [
    path('products/', Products.as_view()),
    path('fridges/', Fridges.as_view()),
]
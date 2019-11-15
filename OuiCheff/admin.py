from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Receipt)
admin.site.register(Product)
admin.site.register(ReceiptHasProduct)
admin.site.register(TimeToEat)
admin.site.register(Fridge)


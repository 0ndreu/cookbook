from django.contrib import admin
from .models import Product, Receipt, ReceiptHasProduct, Fridge


class FridgeAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'how_many')


class ReceiptHasProductAdmin(admin.ModelAdmin):
    list_display = ('receipt', 'product', 'count_of_product')


admin.site.register(Receipt)
admin.site.register(Product)
admin.site.register(ReceiptHasProduct, ReceiptHasProductAdmin)
admin.site.register(Fridge, FridgeAdmin)


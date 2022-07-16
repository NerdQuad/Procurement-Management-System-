from django.contrib import admin
from .models import Product, PurchaseOrder, PurchaseOrderItem, Supplier, PurchaseRequest, PurchaseRequestItem
# Register your models here.

admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItem)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(PurchaseRequest)
admin.site.register(PurchaseRequestItem)
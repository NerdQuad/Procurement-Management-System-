from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('', views.home, name='base'),
    path('contact', views.contact, name='contact'),
    path('profile', views.profile, name='profile'),
    

    #procurement officer authentication and authorization
    path('po_login', views.po_login, name='po_login'),
    path('po_signup', views.po_signup, name='po_signup'), 
    path('po_logout', views.po_logout, name='po_logout'), 


    #main procurement management functionalities 
    path('menu', views.menu, name='menu'),

    #product 
    path('product', views.product, name='product'),
    path('new_product', views.new_product, name='new_product'), 
    path('edit/<int:id>', views.edit_product, name='edit_product'),
    path('update/<int:id>', views.update_product, name='update_product'), 
    path('delete/<int:id>', views.delete_product, name='delete_product'), 


    #purchase request 
    path('purchase_request', views.purchase_request, name='purchase_request'),

    #purchase order
    path('purchase_order', views.purchase_order, name='purchase_order'),


    #supplier 
    path('supplier', views.supplier, name='supplier'), 
    path('new_supplier', views.new_supplier, name='new_supplier'), 
    path('edit_supplier/<int:id>', views.edit_supplier, name='edit_supplier'), 
    path('update_supplier/<int:id>', views.update_supplier, name='update_supplier'),
    path('delete_supplier/<int:id>', views.delete_supplier, name='delete_supplier'), 
]
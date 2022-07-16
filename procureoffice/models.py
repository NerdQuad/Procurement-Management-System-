from django.urls import reverse
from django.db import models
#Create your models here.

#Product Database Table
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=100, decimal_places=2)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name



#Supplier Database Table
class Supplier(models.Model):
    company_name = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=11)
    alternative_phone = models.CharField(max_length=11)
    website = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.company_name
    
    def get_absolute_url(self):
        return reverse('supplier_detail', kwargs = {'pk': self.pk})



#Purchase Request Database Table 
class PurchaseRequest(models.Model):
    STATUS = (
        ('Approved', 'Approved'), 
        ('Pending', 'Pending'), 
        ('Withdrawn', 'Withdrawn'), 
    )
    pr_no = models.AutoField(primary_key=True)
    pr_status = models.CharField(choices=STATUS, max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pr_status

class PurchaseRequestItem(models.Model):
    requester = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    item_name = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=50)
    quantity = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self):
        return self.department



#Purchase Order Database Table
class PurchaseOrder(models.Model):
    purchase_order_id = models.CharField(primary_key=True, max_length=10)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    date_issued = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.supplier



#Purchase Order Items Database Table 
class PurchaseOrderItem(models.Model):
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True) 
    description = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=100, decimal_places=2)
    total_cost = models.DecimalField(max_digits=100, decimal_places=2)
    delivery_date = models.DateField()

    def __str__(self):
        return self.description  





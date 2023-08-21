from django.db import models
from django.utils import timezone
# Create your models here.

#defining category of engine
class Category(models.Model):
    name = models.CharField(max_length = 50, null = False, blank = False,unique=True)
    def __str__(self):
        return self.name
#defining category for product
class Product(models.Model):
#referencing the category of the product
    Category_name = models.ForeignKey(Category,on_delete=models.CASCADE,null=False, blank=False)
    #reserved for date of arrival fields
    part_name = models.CharField(max_length=50, null = False, blank=False)
    country_of_origin = models.CharField(max_length=50,null=False,blank=False)
    total_quantity = models.IntegerField(default=0, null=False, blank=False)
    issued_quantity = models.IntegerField(default=0, null=False,blank=False)
    received_quantity = models.IntegerField(default=0, null=False,blank=False)
    unit_price =models.IntegerField(default=0, null=False,blank=False) 
    arrival_date =models.DateField(default=timezone.now)
    branch_name =models.CharField(max_length=100, null=False,blank=False)
    # part_number = models.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
        return self.part_name 
    

class Sale(models.Model):
    part_purchased = models.ForeignKey(Product,on_delete=models.CASCADE,null=False, blank=False)
    quantity = models.IntegerField(default=0,null=False,blank=False)
    amount_received = models.IntegerField(default=0,null=False,blank=False)
    buyer_names = models.CharField(max_length=100,null=False,blank=False)
    unit_price = models.IntegerField(default=0,null=False,blank=False)
    branch = models.CharField(max_length=100, null=False,blank=False)
    buyer_contact = models.IntegerField(default=0,null=False,blank=False)
    date_of_purchase = models.DateField(default=timezone.now)
    

    def get_total(self):
        total = self.quantity * self.part_purchased.unit_price
        return int(total)
    
    def get_change(self):
        change = self.get_total() -self.amount_received
        return abs(int(change))
    
    def __str__(self):
        return self.part_purchased.part_name
    
    def __str__(self):
        return self.buyer_names
                             
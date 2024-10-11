from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
       
class Menu(models.Model):
    name  = models.CharField(max_length=100)
    category =  models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price =  models.FloatField()
  
class Table(models.Model):
    table_number = models.IntegerField()
    capacity = models.IntegerField()
      
class Waiter(models.Model):
    name = models.CharField(max_length=100)
    
class Order(models.Models):
    table  = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    waiter = models.ForeignKey(Waiter, on_delete=models.SET_NULL, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    quantity  = models.IntegerField()
      
class Reception(models.Model):
    
    name = models.CharField(max_length=100)
    
    
    



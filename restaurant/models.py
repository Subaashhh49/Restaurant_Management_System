from django.db import models

# Create your models here.
 
class Table(models.Model):
     capacity = IntegerField
     table_number = IntegerField
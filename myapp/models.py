from django.db import models

class Product(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'products'

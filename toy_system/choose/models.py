from django.db import models
from django.utils import timezone

# Create your models here.

class Menu(models.Model):
    '''Menu class is for dish object'''
    name = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default = '')

    def __str__(self):
        return self.name

class CustRecord(models.Model):
    '''Each order is a CustRecord object'''
    name = models.CharField(max_length=20)
    time = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    payment = models.BooleanField(default=False)
    table_id = models.IntegerField(default = 0)
    def __str__(self):
        return self.name

class OrderRecord(models.Model):
    '''Each dish in the order is an OrderRecord object'''
    cust_id = models.ForeignKey(CustRecord, on_delete=models.CASCADE,related_name = 'cust_order')
    dish_id = models.ForeignKey(Menu, on_delete=models.CASCADE,related_name = 'dish_order')
    quantity = models.PositiveSmallIntegerField()
    served = models.BooleanField(default=False)

class MenuImage(models.Model):
    photo = models.ImageField(upload_to='menu/')
    menu_image = models.ForeignKey(Menu,related_name='menu_image')

class MenuVideo(models.Model):
    video = models.URLField()
    menu_video = models.ForeignKey(Menu,related_name='menu_video')
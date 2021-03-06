from django.db import models
from django.utils import timezone

# Create your models here.

class Menu(models.Model):
    '''Menu class is for dish object'''
    CATEGORY = (
        ('AP', 'Appetizer'),
        ('MC', 'Main Course'),
        ('DE', 'Dessert'),
        ('BE', 'Beverage'),
    )
    name = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default = '')
    categories = models.CharField(choices=CATEGORY, default = 'Appetizer',max_length = 20)

    def __str__(self):
        return self.name

    def few_reviews(self):
        return self.dish_review.all().order_by('-create_date')[:3]

class CustRecord(models.Model):
    '''Each order is a CustRecord object'''
    name = models.CharField(max_length=20)
    time = models.DateTimeField(default=timezone.now)
    payment = models.BooleanField(default=False)
    table_id = models.IntegerField(default = 0)
    comments = models.TextField(default = '')
    def __str__(self):
        return self.name
    def total_price(self):
        total = 0
        for i in self.cust_order.all():
            if(isinstance(i.quantity, int)==False or i.quantity < 0):
                return -1
            if(i.dish_id.cost < 0):
                return -1
            total += i.quantity * i.dish_id.cost
        return round(total, 2)

class OrderRecord(models.Model):
    '''Each dish in the order is an OrderRecord object'''
    cust_id = models.ForeignKey(CustRecord, on_delete=models.CASCADE,related_name = 'cust_order')
    dish_id = models.ForeignKey(Menu, on_delete=models.CASCADE,related_name = 'dish_order')
    quantity = models.PositiveSmallIntegerField()
    served = models.BooleanField(default=False)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        now = str(self.order_date)
        x = "Order Date: " + now + " ---- Custmer Name:  " + self.cust_id.name
        return x

class Review(models.Model):
    cust_id = models.ForeignKey(CustRecord, on_delete=models.CASCADE,related_name = 'cust_review')
    dish_id = models.ForeignKey(Menu, on_delete=models.CASCADE,related_name = 'dish_review')
    context = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        now = str(self.create_date)
        x = "Review Date: " + now + " ---- Custmer Name:  " + self.cust_id.name
        return x

class MenuImage(models.Model):
    name = models.CharField(max_length=20, default = '')
    photo = models.ImageField(upload_to='menu/')
    menu_image = models.ForeignKey(Menu,related_name='menu_image')
    def __str__(self):
        return self.name

class MenuVideo(models.Model):
    name = models.CharField(max_length=20, default = '')
    video = models.URLField()
    menu_video = models.ForeignKey(Menu,related_name='menu_video')

    def __str__(self):
        return self.name

from django.test import TestCase
from choose.models import *
# Create your tests here.
from django.core.urlresolvers import reverse
from decimal import Decimal

def create_new_dish(name,cost):
    new_dish = Menu(name=name,cost=cost)
    new_dish.save()
    return new_dish

def create_new_record(name):
    new_record = CustRecord(name=name)
    new_record.save()
    return new_record

class TotalPriceMethodTests(TestCase):
    def test_price_with_zero_item(self):
        new_record = create_new_record('test')
        self.assertIs(new_record.total_price(), 0)

    def test_price_with_one_items_one_quantity(self):
    	new_record = create_new_record('test')
    	new_dish = create_new_dish('pie',10.5)
    	new_record.cust_order.create(dish_id = new_dish ,quantity=1)
    	self.assertEqual(new_record.total_price(), 10.5)

    def test_price_with_one_items_multi_quantity(self):
    	new_record = create_new_record('test')
    	new_dish = create_new_dish('pie',10.5)
    	new_record.cust_order.create(dish_id = new_dish ,quantity=3)
    	self.assertEqual(new_record.total_price(), 31.5)

    def test_price_with_multi_items_one_quantity(self):
    	new_record = create_new_record('test')
    	new_dish = create_new_dish('pie',10.5)
    	new_dish2 = create_new_dish('pie_again',3)
    	new_record.cust_order.create(dish_id = new_dish ,quantity=1)
    	new_record.cust_order.create(dish_id = new_dish2 ,quantity=1)
    	self.assertEqual(new_record.total_price(), 13.5)

    def test_price_with_multi_items_multi_quantity(self):
    	new_record = create_new_record('test')
    	new_dish = create_new_dish('pie',10.5)
    	new_dish2 = create_new_dish('pie_again',3)
    	new_record.cust_order.create(dish_id = new_dish ,quantity=2)
    	new_record.cust_order.create(dish_id = new_dish2 ,quantity=2)
    	self.assertEqual(new_record.total_price(), 27)



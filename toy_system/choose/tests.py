from django.test import TestCase
from choose.models import *
# Create your tests here.
from django.core.urlresolvers import reverse
from decimal import Decimal

def create_new_dish(name,cost,description="",categories='Appetizer'):
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
        self.assertIs(new_record.total_price(), 0.0)

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


#Team assignment 4 test case
    def test_price_with_neg_price(self):
        new_record = create_new_record('test')
        new_dish = create_new_dish('Lobster',-100)
        new_dish2 = create_new_dish('Jello',-50)
        new_record.cust_order.create(dish_id = new_dish,quantity=2)
        new_record.cust_order.create(dish_id = new_dish2,quantity=2)
        self.assertEqual(new_record.total_price(), -1)

    def test_price_with_all_neg(self):
        new_record = create_new_record('test')
        new_dish = create_new_dish('Lobster',-100)
        new_dish2 = create_new_dish('Jello',-50)
        new_record.cust_order.create(dish_id = new_dish,quantity=-2)
        new_record.cust_order.create(dish_id = new_dish2,quantity=-2)
        self.assertEqual(new_record.total_price(), -1)

    def test_price_with_all_pos(self):
        new_record = create_new_record('test')
        new_dish = create_new_dish('Lobster',100)
        new_dish2 = create_new_dish('Jello',50)
        new_record.cust_order.create(dish_id = new_dish,quantity=2)
        new_record.cust_order.create(dish_id = new_dish2,quantity=2)
        self.assertEqual(new_record.total_price(), 300)

    def test_price_with_some_pos_some_neg(self):
        new_record = create_new_record('test')
        new_dish = create_new_dish('Lobster',100)
        new_dish2 = create_new_dish('Jello',50)
        new_record.cust_order.create(dish_id = new_dish,quantity=-2)
        new_record.cust_order.create(dish_id = new_dish2,quantity=2)
        self.assertEqual(new_record.total_price(), -1)

    def test_price_with_zero_quan(self):
        new_record = create_new_record('test')
        new_dish = create_new_dish('Lobster',100)
        new_dish2 = create_new_dish('Jello',50)
        new_record.cust_order.create(dish_id = new_dish,quantity=0)
        new_record.cust_order.create(dish_id = new_dish2,quantity=0)
        self.assertEqual(new_record.total_price(), 0)

    def test_price_with_dec_quan(self):
        new_record = create_new_record('test')
        new_dish = create_new_dish('Lobster',100)
        new_dish2 = create_new_dish('Jello',50)
        new_record.cust_order.create(dish_id = new_dish,quantity=2.3)
        new_record.cust_order.create(dish_id = new_dish2,quantity=2.00)
        self.assertEqual(new_record.total_price(), 300)

class MenuTests(TestCase):
    def test_menu_with_one_dish(self):
        new_dish = create_new_dish(name = "apple pie", cost = 1.32)
        self.assertQuerysetEqual(
            Menu.objects.all(),
            ['<Menu: apple pie>']
        )
        self.assertEqual(str(new_dish), "apple pie")
        self.assertEqual(new_dish.categories, 'Appetizer')

    def test_menu_with_zero_dish(self):
        self.assertQuerysetEqual(
            Menu.objects.all(),
            []
        )

class CustRecordTests(TestCase):
    def test_custrecord_with_one(self):
        new_record = create_new_record('test')
        self.assertQuerysetEqual(
            CustRecord.objects.all(),
            ['<CustRecord: test>']
        )

    def test_custrecord_with_zero(self):
        self.assertQuerysetEqual(
            CustRecord.objects.all(),
            []
        )

class OrderRecordTests(TestCase):
    def test_orderrecord_with_one(self):
        new_record = create_new_record('test')
        new_dish = create_new_dish('Lobster',100)
        new_order_record = OrderRecord(cust_id = new_record,dish_id = new_dish, quantity = 1)
        new_order_record.save()
        now = str(new_order_record.order_date)
        x = "Order Date: " + now + " ---- Custmer Name:  " + new_order_record.cust_id.name
        self.assertQuerysetEqual(
            OrderRecord.objects.all(),
            ['<OrderRecord: ' + x + '>']
        )

class ReviewTest(TestCase):
    def test_review_with_one(self):
        new_record = create_new_record('test')
        new_dish = create_new_dish('Lobster',100)
        new_review = Review(cust_id = new_record, dish_id = new_dish,context = 'good!!')
        new_review.save()
        now = str(new_review.create_date)
        x = "Review Date: " + now + " ---- Custmer Name:  " + new_review.cust_id.name
        self.assertQuerysetEqual(
            Review.objects.all(),
            ['<Review: ' + x + '>']
        )

class MenuVideoTest(TestCase):
    def test_video_with_one(self):
        new_dish = create_new_dish('Lobster',100)
        new_video = MenuVideo(name = "new video", video = "https://aaa.abc.com", menu_video = new_dish)
        new_video.save()
        self.assertQuerysetEqual(
            MenuVideo.objects.all(),
            ['<MenuVideo: new video>']
        )
    def test_video_with_zero(self):
        self.assertQuerysetEqual(
            MenuVideo.objects.all(),
            []
        )

class MenuViewTests(TestCase):
    def test_index_view_with_one_dish(self):
        new_dish = create_new_dish(name = "apple pie", cost = 1.32,description="good",categories='Appetizer')
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['list_of_pie'],
            ['<Menu: apple pie>']
        )

    def test_index_view_with_zero_dish(self):
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['list_of_pie'],
            []
        )

class ResultViewTests(TestCase):
    def test_result_view_cust_exist(self):
        new_record = create_new_record('test')
        response = self.client.get(reverse('result',args=(new_record.id,)))
        self.assertQuerysetEqual(
            response.context['cust'],
            ['<CustRecord: test>']
        )

    def test_result_view_cust_not_exist(self):
        cid = 1
        response = self.client.get(reverse('result',args=(cid,)))
        self.assertEqual(response.status_code,404)

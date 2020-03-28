from django.test import TestCase
from tools.models import *
from tools.views import *
import datetime


# Create your tests here.
class ToolCategoryTestCase(TestCase):
    def setUp(self):
        ToolCategory.objects.create(type="hammer", available=3, unavailable=1, price=5.00, tool_image="")

    def test_toolCategory(self):
        hammer = ToolCategory.objects.get(type="hammer")
        self.assertEqual(hammer.price, 5.00)
        self.assertEqual(hammer.type, "hammer")
        self.assertEqual(hammer.available, 3)
        self.assertEqual(hammer.tool_image, "")


class DueDatesTestCase(TestCase):
    def setUp(self):
        hammer = ToolCategory.objects.create(type="hammer", available=3, unavailable=1, price=5.00, tool_image="")
        DueDates.objects.create(toolCategory=hammer, quantity=2, buyer="Mark", date_bought='2020-03-27 09:20',
                                date_due='2020-03-28 09:20')

    def test_dueDate(self):
        d = DueDates.objects.get(buyer="Mark")
        self.assertEqual(d.toolCategory.type, "hammer")
        self.assertEqual(d.quantity, 2)
        self.assertEqual(d.buyer, "Mark")
        self.assertEqual(d.date_bought.replace(tzinfo=None), datetime.datetime(2020, 3, 27, 9, 20, tzinfo=None))
        self.assertEqual(d.date_due.replace(tzinfo=None), datetime.datetime(2020, 3, 28, 9, 20, tzinfo=None))


class ShoppingCartTestCase(TestCase):
    def setUp(self):
        hammer = ToolCategory.objects.create(type="hammer", available=3, unavailable=1, price=5.00, tool_image="")
        ShoppingCart.objects.create(toolCategory=hammer, tool="Hammer", quantity=1)

    def test_shoppingCart(self):
        s = ShoppingCart.objects.get(tool="Hammer")
        self.assertEqual(s.toolCategory.type, 'hammer')
        self.assertEqual(s.tool, 'Hammer')
        self.assertEqual(s.quantity, 1)


class HistoryTestCase(TestCase):
    def setUp(self):
        History.objects.create(customer='Mark', date_bought='2020-03-27 09:20', price=5.00, tools='hammer',
                               state='checkout')

    def test_History(self):
        h = History.objects.get(customer='Mark')
        self.assertEqual(h.customer, 'Mark')
        self.assertEqual(h.date_bought.replace(tzinfo=None), datetime.datetime(2020, 3, 27, 9, 20, tzinfo=None))
        self.assertEqual(h.price, 5.00)
        self.assertEqual(h.tools, 'hammer')
        self.assertEqual(h.state, 'checkout')

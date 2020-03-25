from django.test import TestCase
from tools.models import *

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
        
        
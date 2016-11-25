from django.test import TestCase
from django.core.urlresolvers import resolve
from views import post_list

# Create your tests here.
class SimpleTest(TestCase):

    def test_add_two_numbers(self):
        self.assertEqual(1, 1)


    def test_home_page_view(self):
        home_page = resolve("/")
        self.assertEqual(home_page.func, post_list)
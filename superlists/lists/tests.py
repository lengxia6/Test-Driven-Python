from django.test import TestCase

# Create your tests here.

from django.urls import resolve
from .views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)
#
#     def test_home_page_returns_correct_html(self):
#         request = HttpRequest()
#         response = home_page(request)
#         html = response.conntent.decode('utf8')
#         self.assertTrue('<html>')
#         self.assertIn('<title>To-Do lists</title>',html)
#         self.assertTrue(html.endswitch('</html>'))











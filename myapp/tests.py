from django.test import TestCase
from django.apps import apps
from django.urls import reverse

# Create your tests here.


class MyAppViewTests(TestCase):
    def test_home_page_returns_success_and_expected_content(self):
         response = self.client.get(reverse('home'))

         self.assertEqual(response.status_code, 200)
         self.assertContains(response, "Hello, World!")
         self.assertContains(response, 'home page')

    def test_about_page_returns_success_and_expected_content(self):
         response = self.client.get(reverse('about'))

         self.assertEqual(response.status_code, 200)
         self.assertContains(response, "About Page")
         self.assertContains(response, 'about page')
         
    def test_cats_page_returns_success_and_expected_content(self):
         response = self.client.get(reverse('cats'))

         self.assertEqual(response.status_code, 200)
         self.assertContains(response, "i like cats :)")
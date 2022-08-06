from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book


class BookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', email='test@test.com', password='test')
        self.book = Book.objects.create(
            book_title='good habits',
            purchaser=self.user,
            description="self development"
        )

    def test_list_status(self):
        url = reverse("list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #
    def test_list_template(self):
        url = reverse("list_view")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'list_view.html')

    #
    def test_str_method(self):
        self.assertEqual(str(self.book), 'good habits')

    #
    def test_detail_view(self):
        url = reverse('details_view', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_view.html')

    def test_create_view(self):
        url = "create_view"
        data = {
            "book_title": "physics",
            "purchaser": self.user.id,
            "description": "basic roles in pyhsics",
        }
        response = self.client.post(reverse(url), data, follow=True)
        self.assertRedirects(response, reverse('details_view', args="2"))

    def test_update_view(self):
        response = self.client.post(reverse("update_view", args="1"), {
            "book_title": "physics",
            "purchaser": self.user.id,
            "description": "basic roles in pyhsics",
        }, )
        self.assertRedirects(response, reverse('details_view', args="1"))

    def test_delete_view(self):
        response = self.client.get(reverse("delete_view", args="1"))
        self.assertEqual(response.status_code, 200)

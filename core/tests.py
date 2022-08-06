from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book


class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', email='test@test.com', password='test')
        self.snack = Book.objects.create(
            title='mentos',
            purchaser=self.user,
            description="hot"
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
        self.assertEqual(str(self.snack), 'mentos')

    #
    def test_detail_view(self):
        url = reverse('details_view', args=[self.snack.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_view.html')

    def test_create_view(self):
        url = "create_view"
        data = {
            "title": "Chocolate",
            "purchaser": self.user.id,
            "description": "Details about Chocolate",
        }
        response = self.client.post(reverse(url), data, follow=True)
        self.assertRedirects(response, reverse('details_view', args="2"))

    def test_update_view(self):
        response = self.client.post(reverse("update_view", args="1"), {
            "title": "Choco",
            "purchaser": self.user.id,
            "description": "Details about Chocolate",
        }, )
        self.assertRedirects(response, reverse('details_view', args="1"))

    def test_delete_view(self):
        response = self.client.get(reverse("delete_view", args="1"))
        self.assertEqual(response.status_code, 200)

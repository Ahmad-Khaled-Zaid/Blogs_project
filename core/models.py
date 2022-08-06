from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Book(models.Model):
    book_title = models.CharField(max_length=255)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse('details_view', args=[self.pk])

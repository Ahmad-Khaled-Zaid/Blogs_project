from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
urlpatterns = [
    path('', BookListView.as_view(), name='list_view'),
    path('details/<int:pk>', BookDetailView.as_view(), name='details_view'),
    path('create/', BookCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update_view'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete_view')
]

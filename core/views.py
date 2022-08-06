from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy


class BookListView(ListView):
    template_name = 'list_view.html'
    model = Book


class BookDetailView(DetailView):
    template_name = 'detail_view.html'
    model = Book


class BookCreateView(CreateView):
    template_name = 'create_view.html'
    model = Book
    fields = ["book_title", "purchaser", "description"]


class BookUpdateView(UpdateView):
    template_name = 'update_view.html'
    model = Book
    fields = ["book_title", "purchaser", "description"]


class BookDeleteView(DeleteView):
    template_name = 'delete_view.html'
    model = Book
    success_url = reverse_lazy('list_view')

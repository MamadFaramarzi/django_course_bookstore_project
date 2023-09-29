from django.shortcuts import render ,redirect
from django.views import generic
from .models import Book
from .forms import BookForm


class BookListView(generic.ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = 'books'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'books'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price']
    template_name = "books/book_create.html"
#  or

# class BookCreateView(generic.CreateView):
#     model = Book
#     form_class = BookForm
#     template_name = "books/book_create.html"
#     success_url = ""


class BookUpdateView(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_update.html'
    success_url = ''


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = "/books/"


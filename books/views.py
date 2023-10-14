from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Book, Comment
from .forms import BookForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "books/book_list.html"
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'
#     context_object_name = 'books'

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()
    return render(request, 'books/book_detail.html', {'book': book, 'comments': book_comments})






class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'translator', 'description', 'price', 'cover']
    template_name = "books/book_create.html"


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'translator', 'description', 'price', 'cover']
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book_list")

from django.views.generic import ListView, DetailView
from .models import book 

# Create your views here.
class BookListView(ListView):
    model = book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
class BookDetailView(DetailView):
    model = book
    template_name = 'books/book_detail.html'
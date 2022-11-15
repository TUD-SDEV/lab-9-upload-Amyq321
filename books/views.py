from django.views.generic import ListView, DetailView
from .models import book 
from django.db.models import Q

# Create your views here.
class BookListView(ListView):
    model = book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
class BookDetailView(DetailView):
    model = book
    template_name = 'books/book_detail.html'

class SearchResultsListView(ListView):
    model = book
    context_object_name = 'book_list'
    template_name = 'book/search_results.html'

    def get_queryset(self):
        query= self.request.GET.get('q')
        return book.objects.filter(
            Q(title_icontains=query | Q(author_icontains=query))
        )
    
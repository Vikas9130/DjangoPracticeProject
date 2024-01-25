import django_filters
from .models import Book, Author

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'author': ['exact'],
            'published_date': ['exact'],
            'isbn': ['exact', 'lt', 'lte', 'gt', 'gte'],
        }

class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = {
            'name': ['exact', 'istartswith'],
            'email': ['exact', 'icontains'],
        }
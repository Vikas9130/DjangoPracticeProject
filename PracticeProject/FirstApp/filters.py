# FirstApp/filters.py

import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'author': ['exact'],
            'published_date': ['exact'],
            'isbn': ['exact', 'lt', 'lte', 'gt', 'gte'],
        }

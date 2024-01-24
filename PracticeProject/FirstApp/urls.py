from django.urls import path
from FirstApp.views import AuthorList, AuthorDetails, BookDetail, BookListCreateView
from FirstApp import views

urlpatterns = [
    path("", views.home, name='home'),
    path("authors/", AuthorList.as_view(), name="authors-list"),
    path("authors/<int:author_id>", AuthorDetails.as_view(), name="author-name"),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path("books/<int:book_id>/", BookDetail.as_view(), name="book-detail"),
]

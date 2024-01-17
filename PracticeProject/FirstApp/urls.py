from django.urls import path
from FirstApp import views
from FirstApp.views import AuthorList, BookDetail, BookList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', AuthorList, basename='authors')
router.register(r'books', BookList, basename='books')

urlpatterns = [
    path("", views.home, name='home'),
    path("authors/", views.AuthorList.as_view(), name="authors-list"),
    path("authors/<int:author_id>", views.AuthorDetails.as_view(), name="author-name"),
    path("books/", BookList.as_view(), name="book-list"),
    path("books/<int:book_id>/", BookDetail.as_view(), name="book-detail"),

]

from django.urls import path
from FirstApp.views import AuthorList, AuthorDetails, BookDetail, BookListCreateView,AuthorListCreateView, MasterDataCreateView, MasterDataDetailView
from FirstApp import views

urlpatterns = [
    path("", views.home, name='home'),
    # path("authors/", AuthorList.as_view(), name="authors-list"),
    path("authors/<int:author_id>", AuthorDetails.as_view(), name="author-name"),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('authors/', AuthorListCreateView.as_view(),name='author-list'),
    path("books/<int:book_id>/", BookDetail.as_view(), name="book-detail"),
    path('masterdata/', MasterDataCreateView.as_view(), name='masterdata-list-create'),
    path('masterdata/<int:pk>/', MasterDataDetailView.as_view(), name='masterdata-detail'),
]

from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from FirstApp.models import Author, Book, MasterData
from FirstApp.serializers import BookSerializer, AuthorSerializer, MasterDataSerializer
# Correct import statement for DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from FirstApp.filters import BookFilter, AuthorFilter

# Create your views here.
def home(request):
    html = "<html><body><h1>Hello welcome user!</h1></body></html>"
    return HttpResponse(html)


class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['name']
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if(serializer.is_valid):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class AuthorDetails(APIView):
    def get_object(self, author_id):
        return get_object_or_404(Author, pk=author_id)
    def get(self, request, author_id):
        author = self.get_object(author_id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    def put(self, request, author_id):
        serializer = AuthorSerializer(data=request.data)
        if(serializer.is_valid):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    def delete(self, request, author_id):
        serializer = AuthorSerializer(data=request.data)
        if(serializer.is_valid):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)
class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_object(self, book_id):
        return get_object_or_404(Book, pk=book_id)

    def get(self, request, book_id):
        book = self.get_object(book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, book_id):
        book = self.get_object(book_id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        book = self.get_object(book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter 

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class = AuthorFilter

class MasterDataCreateView(generics.ListCreateAPIView):
    queryset = MasterData.objects.all()
    serializer_class = MasterDataSerializer

class MasterDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MasterData.objects.all()
    serializer_class = MasterDataSerializer

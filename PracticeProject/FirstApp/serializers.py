from rest_framework import serializers
from FirstApp.models import Author, Book, MasterData

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_id','name','email']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = '__all__'

class MasterDataSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    author = AuthorSerializer()
    class Meta:
        model = MasterData
        fields = ['id', 'author', 'book', 'created_date']


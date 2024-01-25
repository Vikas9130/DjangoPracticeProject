from django.db import models
from django.utils import timezone


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13) 

    def __str__(self):
        return self.title

class MasterData(models.Model):
    master_data_id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_created =  models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.author.name} - {self.book.title} - {self.created_date}"

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=255)
    pincode = models.IntegerField(max_length=6)

    def __str__(self):
        return f"{self.street}, {self.pincode}"


class Reader(models.Model):
    reader_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    Address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    



"""
class Library(models.Model):
    library_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=True)

    def __str__(self):
        return self.name
"""
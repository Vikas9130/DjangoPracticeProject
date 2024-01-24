from django.contrib import admin
from django.contrib import admin
from FirstApp.models import Author, Book, Address, Reader

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Address)

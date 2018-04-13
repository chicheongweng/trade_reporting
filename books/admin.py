from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from books.models import Book

class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)

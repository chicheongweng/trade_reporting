from modeltranslation.translator import translator, TranslationOptions
from books.models import Book

class BookTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

translator.register(Book, BookTranslationOptions)
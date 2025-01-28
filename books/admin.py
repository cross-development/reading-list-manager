from django.contrib import admin

from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'status', 'publication_year')
    list_filter = ('author', 'status', 'publication_year')
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)

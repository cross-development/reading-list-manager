from django.contrib import admin

from books.models import Book, Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating', 'status', 'publication_year')
    list_display_links = ('id', 'title')
    list_filter = ('authors', 'status', 'publication_year')
    search_fields = ('title', 'authors')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)

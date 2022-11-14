from django.contrib import admin
from .models import *

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre', 'language')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('genre', 'language')
    list_filter = ('genre', 'language')

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name_author', 'first_name_author')
    list_display_links = ('id', 'last_name_author', 'first_name_author')
    search_fields = ('last_name_author',)

class BookFeedbacksAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_feedback', 'book', 'reader')
    # list_display_links = ('id', 'book_feedback')
    search_fields = ('reader',)
    list_editable = ('book', 'reader')
    list_filter = ('book', 'reader')

admin.site.register(Books, BooksAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Genres)
admin.site.register(Languages)
admin.site.register(BookFeedbacks, BookFeedbacksAdmin)
admin.site.register(Cities)
admin.site.register(Libraries)
admin.site.register(LibBooks)
from django.urls import path
# from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('books', books, name='books'),
    path('books/add', add_book, name='add_book'),
    path('books/<int:id>', book, name='book'),
    # path('accounts/user_registration', user_registration, name='user_registration'),
    path('user_registration', user_registration, name='user_registration'),
    path('library_registration', library_registration, name='library_registration'),
    path('libraries', libraries, name='libraries'),
    path('libraries/<int:id>', library, name='library'),
]
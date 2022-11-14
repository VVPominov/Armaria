from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import Books, Genres, Authors, Languages, BookFeedbacks
from .models import *
from .forms import *
import datetime
# from .forms import UserRegistrationForm


def index(request):
    books = Books.objects.all()
    context = {'books': books, 'title': 'Список книг'}
    return render(request, 'index.html', context)


def books(request):
    books = Books.objects.all()
    n = 1
    for book in books:
        book.number = n
        n += 1
    context = {'books': books, 'title': 'Список книг'}
    return render(request, 'books.html', context)


def book(request, id):
    book = Books.objects.get(id=id)
    feedbacks = BookFeedbacks.objects.filter(book=id)

    if request.method == 'POST':
        new_feedback = AddFeedback(request.POST, request.FILES)

        if new_feedback.is_valid():
            feedback = BookFeedbacks()

            feedback.book = book
            feedback.book_feedback = new_feedback.cleaned_data['book_feedback']
            feedback.book_feedback_date_add = datetime.datetime.now()

            user = request.user
            print(user)
            # feedback_sander = User.
            feedback.reader = request.user
            feedback.save()

            return redirect(request.path)

    else:
        new_feedback = AddFeedback()

    context = {
        'book': book,
        'new_feedback': new_feedback,
        'feedbacks': feedbacks
    }

    return render(request, 'book.html', context)
    # return render(request, 'book.html', {'book': book})


def add_book(request):

    if request.method == 'POST':
        new_form = AddBook(request.POST, request.FILES)

        if new_form.is_valid():
            book = Books()
            author = Authors()
            genre = Genres()
            language = Languages()

            last_name = new_form.cleaned_data['last_name_author']
            first_name = new_form.cleaned_data['first_name_author']
            if not (Authors.objects.filter(
                    last_name_author=last_name).exists()
                    and Authors.objects.filter(
                        first_name_author=first_name).exists()):
                author.last_name_author = new_form.cleaned_data[
                    'last_name_author']
                author.first_name_author = new_form.cleaned_data[
                    'first_name_author']
                author.save()

            gen = new_form.cleaned_data['name_genre']
            if not Genres.objects.filter(name_genre=gen).exists():
                genre.name_genre = new_form.cleaned_data['name_genre']
                genre.save()

            lang = new_form.cleaned_data['book_language']
            if not Languages.objects.filter(book_language=lang).exists():
                language.book_language = new_form.cleaned_data['book_language']
                language.save()

            book.title = new_form.cleaned_data['title']
            book.book_image = new_form.cleaned_data['book_image']
            book.genre = Genres.objects.get(
                name_genre=new_form.cleaned_data['name_genre'])

            first_last_author = Authors.objects.filter(
                last_name_author=new_form.cleaned_data['last_name_author']
            ) & Authors.objects.filter(
                first_name_author=new_form.cleaned_data['first_name_author'])
            book.author = first_last_author[0]
            book.language = Languages.objects.get(
                book_language=new_form.cleaned_data['book_language'])
            book.save()

            return redirect('index')

    else:
        new_form = AddBook()

    return render(request, 'add_book.html', {'new_form': new_form})


def user_registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = User()
            new_user.username = user_form.cleaned_data['username']
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.first_name = user_form.cleaned_data['first_name']
            new_user.last_name = user_form.cleaned_data['last_name']
            new_user.email = user_form.cleaned_data['email']
            new_user.save()
            return render(request, 'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def library_registration(request):
    if request.method == 'POST':
        lib_form = LibRegistrationForm(request.POST, request.FILES)
        if lib_form.is_valid():

            city = Cities()
            town = lib_form.cleaned_data['library_city']
            if not Cities.objects.filter(city_name=town).exists():
                city.city_name = lib_form.cleaned_data['library_city']
                city.save()

            new_lib = Libraries()
            new_lib.library_name = lib_form.cleaned_data['library_name']
            new_lib.library_description = lib_form.cleaned_data['library_description']
            new_lib.library_contacts = lib_form.cleaned_data['library_contacts']
            new_lib.library_city = Cities.objects.get(city_name=lib_form.cleaned_data['library_city'])
            new_lib.library_image = lib_form.cleaned_data['library_image']
            new_lib.save()
            return render(request, 'library_registration_done.html', {'new_lib': new_lib})
            # redirect('index')
    else:
        lib_form = LibRegistrationForm()

    context = {'lib_form': lib_form}

    return render(request, 'library_registration.html', context)

def libraries(request):
    libraries = Libraries.objects.all()
    n = 1
    for library in libraries:
        library.number = n
        n += 1
    context = {'libraries': libraries, 'title': "Список домашних библиотек"}
    return render(request, 'libraries.html', context)

def library(request, id):
    library = Libraries.objects.get(id=id)
    context = {'library': library, 'title': "Домашняя библиотека"}
    return render(request, 'library.html', context)
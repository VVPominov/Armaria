from email.mime import image
from email.policy import default
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.ForeignKey('Authors',
                               on_delete=models.PROTECT,
                               null=True,
                               verbose_name='Авторы')
    genre = models.ForeignKey('Genres',
                              on_delete=models.PROTECT,
                              null=True,
                              verbose_name='Жанры')
    language = models.ForeignKey('Languages',
                                 on_delete=models.PROTECT,
                                 null=True,
                                 verbose_name='Языки')
    book_image = models.ImageField(upload_to='book_images/',
                                   blank=True,
                                   verbose_name='Изображения книги')
    definition = models.CharField(max_length=300,
                                  verbose_name='Краткое описание',
                                  default=" ",
                                  blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = [
            'title',
        ]


class Authors(models.Model):
    last_name_author = models.CharField(max_length=50,
                                        db_index=True,
                                        verbose_name='Фамилия автора')
    first_name_author = models.CharField(max_length=50,
                                         db_index=True,
                                         verbose_name='Имя автора')

    def __str__(self):
        return f'{self.first_name_author} {self.last_name_author}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['last_name_author']


class Genres(models.Model):
    name_genre = models.CharField(max_length=50,
                                  db_index=True,
                                  verbose_name='Жанр')

    def __str__(self):
        return self.name_genre

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name_genre']


class Languages(models.Model):
    book_language = models.CharField(max_length=50,
                                     db_index=True,
                                     verbose_name='Язык')

    def __str__(self):
        return self.book_language

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class BookFeedbacks(models.Model):
    book = models.ForeignKey('Books',
                             on_delete=models.PROTECT,
                             null=True,
                             verbose_name='Книга')
    book_feedback = models.TextField(verbose_name='Отзыв по книге',
                                     default="",
                                     blank=False)
    book_feedback_date_add = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации')

    reader = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               null=True,
                               verbose_name='Читатель')

    def __str__(self):
        return self.book_feedback

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-book_feedback_date_add']

class Cities(models.Model):
    city_name = models.CharField(max_length=50,
                                  db_index=True,
                                  verbose_name='Город')

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['city_name']


class Libraries(models.Model):
    # library_reader = models.OneToOneField(User, on_delete = models.CASCADE, default='2')
    library_name = models.CharField(max_length=50, db_index=True, verbose_name='Название библиотеки')
    library_image = models.ImageField(upload_to='library_images/', blank=True, verbose_name='Обложка библиотеки')
    library_description = models.CharField(max_length=300, verbose_name='Описание библиотеки', default=" ", blank=False)
    library_contacts = models.CharField(max_length=200, db_index=True, verbose_name='Контакты библиотеки')
    library_city = models.ForeignKey("Cities", on_delete=models.PROTECT, null=True, verbose_name='Город')

    def __str__(self):
        return self.library_name

    class Meta:
        verbose_name = 'Домащняя библиотека'
        verbose_name_plural = 'Домашние библиотеки'
        ordering = ['library_name']

class LibBooks(models.Model):

    BOOK_STATUS = [('Read', 'Дам почитать'), ('Change', 'Поменяю'), ('Sell', 'Продам')]
    BOOK_STATE = [('Read', 'В аренде'), ('Change', 'Доступна'), ('Sell', 'Продана')]
    BOOK_VISIBALITY = [('Visibale', 'Видима'), ('Invisibale', 'Невидима')]

    library = models.ForeignKey("Libraries", on_delete=models.PROTECT, null=True, verbose_name='Домашняя библиотека')
    book = models.ForeignKey("Books", on_delete=models.PROTECT, null=True, verbose_name='Книга в либе')
    book_status = models.CharField(choices=BOOK_STATUS, max_length=10)
    book_state = models.CharField(choices=BOOK_STATE, max_length=10)
    book_visibality = models.CharField(choices=BOOK_VISIBALITY, max_length=10)

    def __str__(self):
        return self.book.title

    class Meta:
        verbose_name = 'Книга библиотеки'
        verbose_name_plural = 'Книги библиотеки'



    


# book_id
# book_status_id
# book_state_id
# book_visibality_id
    # books = models.ForeignKey('Books', on_delete=models.PROTECT, null=True, verbose_name='Книга')
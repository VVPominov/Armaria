# Generated by Django 4.1.2 on 2022-10-26 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homelib', '0009_books_definition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['title'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.CreateModel(
            name='BookFeedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_feedback', models.TextField(default='', verbose_name='Отзыв по книге')),
                ('book_feedback_date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('book_feedback_date_upd', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='homelib.books', verbose_name='Книга')),
            ],
        ),
    ]

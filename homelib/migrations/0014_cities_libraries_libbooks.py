# Generated by Django 4.1.2 on 2022-10-29 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homelib', '0013_alter_bookfeedbacks_reader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(db_index=True, max_length=50, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Libraries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library_name', models.CharField(db_index=True, max_length=50, verbose_name='Название библиотеки')),
                ('library_image', models.ImageField(blank=True, upload_to='library_images/', verbose_name='Обложка библиотеки')),
                ('library_description', models.CharField(default=' ', max_length=300, verbose_name='Краткое описание библиотеки')),
                ('library_contacts', models.CharField(db_index=True, max_length=200, verbose_name='Контакты')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='homelib.cities', verbose_name='Читатель')),
            ],
        ),
        migrations.CreateModel(
            name='LibBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_status', models.CharField(choices=[('Read', 'Дам почитать'), ('Change', 'Поменяю'), ('Sell', 'Продам')], max_length=10)),
                ('book_state', models.CharField(choices=[('Read', 'В аренде'), ('Change', 'Доступна'), ('Sell', 'Продана')], max_length=10)),
                ('book_visibality', models.CharField(choices=[('Visibale', 'Видима'), ('Invisibale', 'Невидима')], max_length=10)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='homelib.books', verbose_name='Книга в либе')),
            ],
        ),
    ]

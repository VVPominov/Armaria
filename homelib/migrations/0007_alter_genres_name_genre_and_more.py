# Generated by Django 4.1.2 on 2022-10-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homelib', '0006_alter_authors_first_name_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='name_genre',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='languages',
            name='book_language',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Язык'),
        ),
    ]

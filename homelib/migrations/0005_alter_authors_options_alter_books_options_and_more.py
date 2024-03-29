# Generated by Django 4.1.2 on 2022-10-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homelib', '0004_alter_authors_surname_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authors',
            options={'ordering': ['last_name_author'], 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['author'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.RemoveField(
            model_name='authors',
            name='name_author',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='surname_author',
        ),
        migrations.AddField(
            model_name='authors',
            name='first_name_author',
            field=models.CharField(db_index=True, default='w', max_length=50, verbose_name='Имя автора'),
        ),
        migrations.AddField(
            model_name='authors',
            name='last_name_author',
            field=models.CharField(db_index=True, default='q', max_length=50, verbose_name='Фамилия автора'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-29 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homelib', '0017_alter_libraries_library_reader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraries',
            name='library_reader',
            field=models.OneToOneField(default='2', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
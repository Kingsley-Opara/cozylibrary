# Generated by Django 4.0.5 on 2022-07-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cozylibrary', '0011_remove_book_category_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book',
            field=models.FileField(upload_to='books/'),
        ),
    ]

# Generated by Django 5.1 on 2024-08-28 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_rename_genre_film_genre_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genre_ids',
            field=models.ManyToManyField(null=True, to='films.filmgenre'),
        ),
    ]

# Generated by Django 5.1 on 2024-08-30 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_alter_film_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.CharField(max_length=10),
        ),
    ]

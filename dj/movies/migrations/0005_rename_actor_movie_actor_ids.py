# Generated by Django 4.2.7 on 2023-11-19 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_remove_movie_director_movie_director'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actor',
            new_name='actor_ids',
        ),
    ]

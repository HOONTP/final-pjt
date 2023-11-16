# Generated by Django 4.2.7 on 2023-11-16 02:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre_ids',
            field=models.ManyToManyField(blank=True, null=True, related_name='genremovie', to='movies.genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_movie', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='like_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_Review', to=settings.AUTH_USER_MODEL),
        ),
    ]
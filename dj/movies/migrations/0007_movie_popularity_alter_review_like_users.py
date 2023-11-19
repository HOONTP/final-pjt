# Generated by Django 4.2.7 on 2023-11-19 12:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0006_alter_movie_like_users_alter_review_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='popularity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='like_users',
            field=models.ManyToManyField(related_name='like_Reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]

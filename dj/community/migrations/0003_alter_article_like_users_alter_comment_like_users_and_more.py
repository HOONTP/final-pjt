# Generated by Django 4.2.7 on 2023-11-20 00:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_alter_comment_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='like_users',
            field=models.ManyToManyField(related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='like_users',
            field=models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reply',
            name='like_users',
            field=models.ManyToManyField(related_name='like_replies', to=settings.AUTH_USER_MODEL),
        ),
    ]

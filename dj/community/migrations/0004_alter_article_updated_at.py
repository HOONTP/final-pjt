# Generated by Django 4.2.7 on 2023-11-22 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_alter_article_like_users_alter_comment_like_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]

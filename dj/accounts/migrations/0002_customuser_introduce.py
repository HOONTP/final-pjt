# Generated by Django 4.2.7 on 2023-11-22 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='introduce',
            field=models.TextField(blank=True, null=True),
        ),
    ]

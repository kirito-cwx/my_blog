# Generated by Django 2.1.5 on 2023-07-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

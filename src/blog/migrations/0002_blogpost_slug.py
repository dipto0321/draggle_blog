# Generated by Django 2.2 on 2019-11-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='lorem-ipsum'),
            preserve_default=False,
        ),
    ]
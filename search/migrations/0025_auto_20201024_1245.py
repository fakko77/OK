# Generated by Django 3.1.1 on 2020-10-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0024_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
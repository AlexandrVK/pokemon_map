# Generated by Django 3.1.14 on 2023-05-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20230505_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(null=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sherly_app', '0023_societe_nif_societe_phrase'),
    ]

    operations = [
        migrations.AddField(
            model_name='famille',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

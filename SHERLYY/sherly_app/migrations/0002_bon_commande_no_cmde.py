# Generated by Django 5.0.1 on 2024-01-20 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sherly_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bon_commande',
            name='no_cmde',
            field=models.CharField(default='DEFAULT_VALUE', editable=False, max_length=20, unique=True),
        ),
    ]
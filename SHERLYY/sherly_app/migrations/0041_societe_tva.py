# Generated by Django 5.0.1 on 2024-02-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sherly_app", "0040_facture_tva"),
    ]

    operations = [
        migrations.AddField(
            model_name="societe",
            name="tva",
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-24 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sherly_app", "0058_bon_commande_add_d_bon_commande_add_g"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bon_commande",
            name="add_d",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="bon_commande",
            name="add_g",
            field=models.FloatField(default=0),
        ),
    ]

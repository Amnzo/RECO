# Generated by Django 5.0.1 on 2024-02-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sherly_app", "0054_table_bl_date_table_bl_information_acheteur_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="facture",
            name="date",
            field=models.CharField(
                blank=True, default="DATE", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="facture",
            name="n_facture",
            field=models.CharField(
                blank=True, default="Nº FACTURE", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="facture",
            name="notice",
            field=models.CharField(
                blank=True, default="REMARQUE", max_length=50, null=True
            ),
        ),
    ]

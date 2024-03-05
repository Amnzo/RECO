# Generated by Django 5.0.1 on 2024-02-06 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sherly_app", "0042_facture_paye1_facture_paye2_facture_paye3_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facture",
            name="facture1",
            field=models.CharField(
                blank=True, default="SCROTIS  OPTIC 2000 ", max_length=50, null=True
            ),
        ),
        migrations.AlterField(
            model_name="facture",
            name="facture2",
            field=models.CharField(
                blank=True, default="38 rue Saint Denis", max_length=50, null=True
            ),
        ),
        migrations.AlterField(
            model_name="facture",
            name="facture3",
            field=models.CharField(
                blank=True, default="92700 COLOMBES", max_length=50, null=True
            ),
        ),
        migrations.AlterField(
            model_name="facture",
            name="facture4",
            field=models.CharField(
                blank=True, default="FRANCE", max_length=50, null=True
            ),
        ),
        migrations.AlterField(
            model_name="facture",
            name="facture5",
            field=models.CharField(
                blank=True, default="Numero TVA Intraceo", max_length=50, null=True
            ),
        ),
        migrations.AlterField(
            model_name="facture",
            name="facture6",
            field=models.CharField(
                blank=True, default="FR7547911891", max_length=50, null=True
            ),
        ),
        migrations.AlterField(
            model_name="facture",
            name="tva",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

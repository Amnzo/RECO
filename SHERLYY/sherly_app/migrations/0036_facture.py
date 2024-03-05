# Generated by Django 4.2.9 on 2024-02-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sherly_app', '0035_merge_20240205_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col1', models.CharField(default='Désignation', max_length=20)),
                ('col2', models.CharField(default='Qté', max_length=20)),
                ('col3', models.CharField(default='P.Ht', max_length=20)),
                ('col4', models.CharField(default='% Remise', max_length=20)),
                ('col5', models.CharField(default='Montant Remise', max_length=20)),
                ('col6', models.CharField(default='P.U.net Ht', max_length=20)),
                ('col7', models.CharField(default='Facture en EUR', max_length=20)),
                ('col8', models.CharField(default='%TVA', max_length=20)),
                ('facture1', models.CharField(default='SCROTIS  OPTIC 2000 ', max_length=50)),
                ('facture2', models.CharField(default='38 rue Saint Denis', max_length=50)),
                ('facture3', models.CharField(default='92700 COLOMBES', max_length=50)),
                ('facture4', models.CharField(default='FRANCE', max_length=50)),
                ('facture5', models.CharField(default='Numero TVA Intraceo', max_length=50)),
                ('facture6', models.CharField(default='FR7547911891', max_length=50)),
                ('nif_facture', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
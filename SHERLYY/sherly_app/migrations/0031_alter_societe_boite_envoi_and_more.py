# Generated by Django 4.2.9 on 2024-01-29 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sherly_app', '0030_societe_boite_envoi_societe_boite_reception'),
    ]

    operations = [
        migrations.AlterField(
            model_name='societe',
            name='boite_envoi',
            field=models.EmailField(default='gestionrecrutement@hotmail.com', error_messages={'invalid': "L'adresse email de boite d'envoi est invalide."}, max_length=100),
        ),
        migrations.AlterField(
            model_name='societe',
            name='boite_reception',
            field=models.EmailField(default='optiquejaures@hotmail.com', error_messages={'invalid': "L'adresse email de boite de réception est invalide."}, max_length=100),
        ),
    ]
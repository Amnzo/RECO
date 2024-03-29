# Generated by Django 5.0.1 on 2024-02-09 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sherly_app", "0045_facture_remarque"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email_host_user", models.EmailField(max_length=254)),
                ("email_host_password", models.CharField(max_length=100)),
            ],
        ),
    ]

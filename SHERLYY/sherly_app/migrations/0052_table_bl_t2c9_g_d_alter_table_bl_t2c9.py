# Generated by Django 5.0.1 on 2024-02-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sherly_app", "0051_table_bl_t2c10"),
    ]

    operations = [
        migrations.AddField(
            model_name="table_bl",
            name="t2c9_g_d",
            field=models.CharField(default="D/G", max_length=100),
        ),
        migrations.AlterField(
            model_name="table_bl",
            name="t2c9",
            field=models.CharField(default="Oeil", max_length=100),
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sherly_app", "0052_table_bl_t2c9_g_d_alter_table_bl_t2c9"),
    ]

    operations = [
        migrations.AlterField(
            model_name="table_bl",
            name="t1c1",
            field=models.CharField(default="BL", max_length=100),
        ),
        migrations.AlterField(
            model_name="table_bl",
            name="t1c3",
            field=models.CharField(default="CMDE", max_length=100),
        ),
    ]
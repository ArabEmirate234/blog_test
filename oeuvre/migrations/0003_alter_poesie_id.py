# Generated by Django 5.1.3 on 2024-11-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oeuvre", "0002_auto_20200701_1144"),
    ]

    operations = [
        migrations.AlterField(
            model_name="poesie",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
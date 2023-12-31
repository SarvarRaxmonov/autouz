# Generated by Django 4.2.1 on 2023-08-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("car", "0002_cardetail_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardetail",
            name="currency",
            field=models.CharField(
                choices=[("usd", "USD"), ("eur", "EUR"), ("uzs", "UZS")],
                default="uzs",
                max_length=10,
            ),
        ),
    ]

# Generated by Django 4.2.4 on 2024-02-06 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0007_alter_affiliateproduct_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="pinterestboard",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.affiliatecategory",
            ),
        ),
    ]

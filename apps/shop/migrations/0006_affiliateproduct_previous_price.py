# Generated by Django 4.2.4 on 2024-02-06 01:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0005_alter_affiliateproduct_affiliate_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="affiliateproduct",
            name="previous_price",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_blog_readability_analysis_blog_readability_score"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="cornerstone_content",
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.1 on 2023-03-01 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Trip_review", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="score",
            new_name="rating",
        ),
    ]

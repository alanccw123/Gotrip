# Generated by Django 4.1 on 2023-03-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Trip_review", "0002_rename_score_review_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="delete_status",
            field=models.SmallIntegerField(choices=[(0, "normal"), (1, "deleted")]),
        ),
    ]
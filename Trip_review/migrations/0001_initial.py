# Generated by Django 4.1 on 2023-03-01 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trip",
            fields=[
                ("Trip_id", models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("User_id", models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("Review_id", models.IntegerField(primary_key=True, serialize=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("score", models.IntegerField(default=0)),
                ("content", models.CharField(max_length=500)),
                (
                    "delete_status",
                    models.SmallIntegerField(choices=[(1, "normal"), (2, "deleted")]),
                ),
                (
                    "Trip_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Trip_review.trip"
                    ),
                ),
                (
                    "User_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Trip_review.user"
                    ),
                ),
            ],
        ),
    ]

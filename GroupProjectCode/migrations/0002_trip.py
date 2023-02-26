# Generated by Django 4.1.7 on 2023-02-26 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("GroupProjectCode", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trip",
            fields=[
                (
                    "id",
                    models.IntegerField(default=0, primary_key=True, serialize=False),
                ),
                ("tripname", models.CharField(max_length=10)),
                ("introduction", models.CharField(max_length=500)),
                ("imageurl", models.CharField(max_length=500)),
                ("bookednum", models.IntegerField(default=0)),
                ("price", models.IntegerField(default=0)),
            ],
        ),
    ]

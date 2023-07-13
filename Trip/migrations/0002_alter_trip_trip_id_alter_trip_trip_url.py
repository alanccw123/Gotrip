# Generated by Django 4.1.7 on 2023-03-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Trip", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trip",
            name="trip_id",
            field=models.AutoField(
                primary_key=True, serialize=False, verbose_name="商品唯一id"
            ),
        ),
        migrations.AlterField(
            model_name="trip",
            name="trip_url",
            field=models.ImageField(upload_to="imgurl"),
        ),
    ]
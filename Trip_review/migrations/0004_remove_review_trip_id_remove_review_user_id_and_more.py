# Generated by Django 4.1.7 on 2023-03-20 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Trip", "0002_alter_trip_trip_id_alter_trip_trip_url"),
        ("Trip_review", "0003_alter_review_delete_status"),
    ]

    operations = [
        migrations.RemoveField(model_name="review", name="Trip_id",),
        migrations.RemoveField(model_name="review", name="User_id",),
        migrations.AddField(
            model_name="review",
            name="Trip",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="Trip.trip"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="review",
            name="User",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(name="Trip",),
        migrations.DeleteModel(name="User",),
    ]

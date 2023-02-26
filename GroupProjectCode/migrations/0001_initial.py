# Generated by Django 4.1 on 2023-02-26 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('status', models.CharField(default='In process', max_length=128)),
                ('price', models.IntegerField()),
                ('trip', models.CharField(max_length=128)),
                ('user', models.IntegerField()),
            ],
        ),
    ]

from django.db import models


# Create your models here.

class Trip(models.Model):
    Trip_id = models.BigIntegerField(primary_key=True)
    tripname = models.CharField(max_length=200)
    introduction = models.CharField(max_length=200)
    delete_status = models.BooleanField(default=0)
    img_url = models.CharField(max_length=200)
    booked_num = models.IntegerField(default=0)
    Trip_price = models.IntegerField(default=0)


class User(models.Model):
    User_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.IntegerField(default=0)
    # leve = models


class Review(models.Model):
    Review_id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    content = models.CharField(max_length=500)
    delete_choices = (
        (0, "normal"),
        (1, "deleted"),
    )
    delete_status = models.SmallIntegerField(choices=delete_choices)
    Trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)



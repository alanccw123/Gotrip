from django.db import models


# Create your models here.

# class Trip(models.Model):
#     id = models.IntegerField( primary_key=True)
#     tripName = models.CharField( max_length=50)
#     introduction = models.CharField( max_length=500)
#     imageUrl = models.URLField( max_length=200)
#     bookedNum = models.IntegerField()
#     price = models.IntegerField()
#     delete_choices = (
#         (1, "deleted"),
#         (2, "normal"),
#     )
#     delete_status = models.SmallIntegerField(choices=delete_choices)
#
#
# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     userName = models.CharField(max_length=100)
#     password = models.IntegerField()
#     level = models.BooleanField()
#
#
# class Review(models.Model):
#     Review_id = models.IntegerField(primary_key=True)
#     date = models.DateTimeField(auto_now_add=True)
#     score = models.IntegerField()
#     content = models.CharField(max_length=500)
#     delete_choices = (
#         (1, "normal"),
#         (2, "deleted"),
#     )
#     delete_status = models.SmallIntegerField(choices=delete_choices, default=1)
#     Trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE, default=0)
#     User_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

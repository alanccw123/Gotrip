from django.db import models


# Create your models here.
# class User(models.Model):
#     User_id = models.IntegerField(primary_key=True)
#     username = models.CharField(max_length=10)
#     password = models.CharField(max_length=8)
#     level = models.IntegerField()
#
#
# class Trip(models.Model):
#     Trip_id = models.IntegerField(primary_key=True)
#     tripname = models.CharField(max_length=10)
#     introduction = models.CharField(max_length=500)
#     delete_status = models.CharField(max_length=500)
#     image_url = models.ImageField(upload_to='imgurl')
#     booked_num = models.IntegerField(null=True)
#     Trip_price = models.IntegerField()
#
#
# class Review(models.Model):
#     Review_id = models.IntegerField(primary_key=True)
#     date = models.CharField(max_length=10)
#     rating = models.IntegerField()
#     content = models.CharField(max_length=500)
#     delete_status = models.CharField(max_length=2)
#     Trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
#     User_id = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class Order(models.Model):
#     Order_id = models.IntegerField(primary_key=True)
#     amount = models.IntegerField()
#     time = models.DateTimeField()
#     status = models.CharField(default='In process', max_length=50)
#     Order_price = models.IntegerField()
#     Trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True)
#     User_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#
#
# # User1 = User.objects.create(User_id=50, username="Ryan", password="12345", level=0)
# # Trip1 = Trip.objects.create(Trip_id=50, tripname="London", introduction="happy", delete_status="1", image_url="1",
# #                             booked_num=1, Trip_price=1)
# # Order1 = Order.objects.create(Order_id=50, amount=10, time="12：00", status="finished", Order_price=100,
# #                               Trip_id=Trip1, User_id=User1)
# # Review.objects.create(id=1, date="2023.1.1", score=10, content="London is a good place to take photos!", deletestatus=1)
#
#
# # class Comment(models.Model):
# # class Order(models.Model):
# # class Trip(models.Model):
# # class admin(models.Model):

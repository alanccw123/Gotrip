from django.db import models


# Create your models here.
class User(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    Username = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
    level = models.IntegerField(default=0)


class Review(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    date = models.CharField(max_length=10)
    score = models.IntegerField(default=0)
    content = models.CharField(max_length=500)
    deletestatus = models.CharField(max_length=2)


class Trip(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    tripname = models.CharField(max_length=10)
    introduction = models.CharField(max_length=500)
    imageurl = models.CharField(max_length=500)
    bookednum = models.IntegerField(default=0)
    price = models.IntegerField(default=0)



#User.objects.create(id=3, Username="Ryan", password="123456", level=1)
#Review.objects.create(id=1, date="2023.1.1", score=10, content="London is a good place to take photos!", deletestatus=1)


#class Comment(models.Model):
#class Order(models.Model):
#class Trip(models.Model):
#class admin(models.Model):


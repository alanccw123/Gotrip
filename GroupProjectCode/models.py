from django.db import models

# Create your models here.
class Order(models.Model):
    
    amount = models.IntegerField()
    time = models.DateTimeField()
    status = models.CharField(default='In process', max_length=128)
    price = models.IntegerField()
    trip = models.CharField(max_length=128)
    user = models.IntegerField()

    # todo: connect to User models
    # trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self): 
        return str(self.id) 

from django.db import models
from Trip.models import Trip
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    
    amount = models.IntegerField()
    time = models.DateTimeField()
    status = models.CharField(default='In process', max_length=128)
    price = models.IntegerField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Added for the testing chapter.
        if self.amount < 0:
            self.amount = 0
        if self.price < 0:
            self.price = 0;
        super(Order, self).save(*args, **kwargs)
    
    def __str__(self): 
        return str(self.id) 
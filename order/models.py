from django.db import models

# Create your models here.
class Order(models.Model):
    
    amount = models.IntegerField()
    time = models.DateTimeField()
    status = models.CharField(default='In process', max_length=128)
    price = models.IntegerField()
    # trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    trip = models.CharField(max_length=128)
    user = models.IntegerField()

    def save(self, *args, **kwargs):
        # Added for the testing chapter.
        if self.amount < 0:
            self.amount = 0
        if self.price < 0:
            self.price = 0;
        super(Order, self).save(*args, **kwargs)
    
    def __str__(self): 
        return str(self.id) 
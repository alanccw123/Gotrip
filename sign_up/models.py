from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.



class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username
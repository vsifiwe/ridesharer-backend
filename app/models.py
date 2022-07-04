from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Route(models.Model):
    username = models.ForeignKey(Account, on_delete=CASCADE)
    start_lat = models.CharField(max_length=100)
    start_lon = models.CharField(max_length=100)
    end_lat = models.CharField(max_length=100)
    end_lon = models.CharField(max_length=100)
    from_name = models.CharField(max_length=100)
    to_name = models.CharField(max_length=100)

    def __str__(self):
        return self.start_lat + ' ' + self.end_lat

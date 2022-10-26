from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

status = (
    ("PENDING", "Pending"),
    ("CLOSED", "Closed"),
    
)

class Movie(models.Model):
    title  = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500, default=None)

    def __str__(self):
	    return self.title


class Order(models.Model):
    product = models.ForeignKey(Movie, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=status, max_length=155, default="pending")
    price = models.FloatField(default=1.0)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.product.title, self.id)

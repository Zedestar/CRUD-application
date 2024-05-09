from django.db import models

# Create your models here.

class record(models.Model):
    def __str__(self):
        return self.first_name + "  " + self.last_name
    day_created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


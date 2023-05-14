from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ville = models.CharField(max_length=100)
    image = models.CharField(max_length=10000)

    def __str__(self):
        return self.name

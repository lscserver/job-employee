from django.db import models

# Create your models here.
class Home(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.full_name

from django.db import models

# Create your models here.

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    feedback=models.CharField(max_length=100)

    def __str__(self):
        return self.name


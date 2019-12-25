from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=600)


# Create your models here.

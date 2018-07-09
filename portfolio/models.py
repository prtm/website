
# core django
from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Message(TimeStampedModel):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name

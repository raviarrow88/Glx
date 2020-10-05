from django.db import models
from .timeStamp import TimeStamp


class State(TimeStamp):
    name = models.CharField(max_length=255,verbose_name='State')


    def __str__(self):
        return self.name

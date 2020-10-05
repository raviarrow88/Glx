from django.db import models
from .timeStamp import TimeStamp
from .state import State

class City(TimeStamp):
    name = models.CharField(max_length=255,verbose_name='City')
    state = models.ForeignKey(State,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.name

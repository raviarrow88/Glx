from django.db import models
from .timeStamp import TimeStamp
from .city import City
from .address import GeoPosition

class RootState(TimeStamp,GeoPosition):
    start_point = models.ForeignKey(City,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.id)

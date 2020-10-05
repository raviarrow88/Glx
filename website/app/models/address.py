from django.db import models
from .timeStamp import TimeStamp
from .city import City
from .zipCode import ZipCode

class GeoPosition(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name="Latitude",null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name="Longitude",null=True)

    class Meta:
        abstract=True

class Address(GeoPosition,TimeStamp):
    address = models.CharField(max_length=255,verbose_name='Address')
    city = models.ForeignKey(City,on_delete=models.SET_NULL,null=True)
    zip = models.ForeignKey(ZipCode,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return "{}-{}-{}-{}".format(self.address,self.city,self.zip,self.city.state)

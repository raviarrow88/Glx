from django.db import models
from .timeStamp import TimeStamp


class ZipCode(TimeStamp):
    code = models.CharField(max_length=255,verbose_name='Zipcode')


    def __str__(self):
        return self.code

from django.db import models
from .timeStamp import TimeStamp
from django.template.defaultfilters import slugify
from .address import Address
class Agent(TimeStamp):
    agent_id = models.CharField(max_length=10,unique=True,verbose_name='Agent ID')
    agent_name = models.CharField(max_length=255,verbose_name='Agent Name')
    address= models.ForeignKey(Address,verbose_name='Address',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return "{}-{}".format(self.agent_id,self.agent_name)

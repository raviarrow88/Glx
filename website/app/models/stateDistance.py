from django.db import models
from .rootState import RootState
from .timeStamp import TimeStamp
from .agent import Agent

class Distance(TimeStamp):
    source = models.ForeignKey(RootState,on_delete=models.SET_NULL,null=True)
    agent= models.ForeignKey(Agent,on_delete=models.SET_NULL,null=True)
    distance = models.DecimalField(max_digits=15,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return "{}-{}-{}".format(self.source.start_point.state.name,self.agent,self.distance)

from django.db import  models

class TimeStamp(models.Model):
    created_ts = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_ts = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

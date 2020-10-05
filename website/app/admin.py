from django.contrib import admin

# Register your models here.
from .models.agent import Agent
from .models.city import City
from .models.state import State
from .models.rootState import RootState
from .models.address import Address
from .models.stateDistance import Distance
class CitySearch(admin.ModelAdmin):
    search_fields=['name']


admin.site.register(Agent)
admin.site.register(City,CitySearch)
admin.site.register(State)
admin.site.register(RootState)
admin.site.register(Address)
admin.site.register(Distance)

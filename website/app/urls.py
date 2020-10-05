from django.urls import path
from .views import index,createAgents,generateLatLong,calculateDistance,nearestAgents
urlpatterns = [
    # path('', index,name='index'),
    path('',createAgents,name='create_agents'),
    path('generate_lat_long/',generateLatLong,name='gen_lat_long'),
    path('cal_distance/',calculateDistance,name='cal_distance'),
    path('nearest_agents/<id>',nearestAgents,name='nearest_agents'),
]

from django.shortcuts import render,get_object_or_404
import pandas as pd
from django.http import HttpResponse
from .models.state import State
from .models.city import City
from .models.zipCode import ZipCode
from .models.address import Address
from .models.agent import Agent

from django.urls import reverse
import json
from .models.rootState import RootState

def index(request):
    states = RootState.objects.all()
    return render(request,'base.html',context={"states":states})

#function creates the agents data from tsv file
def createAgents(request):
    try:
        if request.POST and request.FILES:
            file = request.FILES.get('file')
            data = pd.read_csv(file,sep='\t',header=None)

            data_list = data.values.tolist()[1:]

            for row in data_list:
                state,created = State.objects.get_or_create(name = row[5])

                city,created= City.objects.get_or_create(name=row[3],state=state)

                zip,created = ZipCode.objects.get_or_create(code=row[4])

                address = Address.objects.create(
                address=row[2],
                city=city,
                zip=zip
                )

                address.save()

                agent = Agent.objects.create(
                agent_id=row[0],
                address=address,
                agent_name=row[1]
                )

                agent.save()

            return redirect(reverse('index'))

        else:
            states = RootState.objects.all()
            return render(request,'upload_agents.html',context={'states':states})
    except Exception as e:
        return HttpResponse(json.dumps({"message":str(e)}))

import requests
from django.http import JsonResponse


#function generates lat and long from agents address
def generateLatLong(request):
    agents = Agent.objects.all()

    for agent in agents:
        get_lat_long(agent)


    return JsonResponse({"message":"Successfully Created Lats & Longs for Agents" })


#helper function
from django.conf import settings
import time
def get_lat_long(agent):
    try:
        url = 'https://geocoder.ls.hereapi.com/6.2/geocode.json'

        params = {'apiKey':settings.GEOCODE_API_KEY,'searchText':"{},{},{},{}".format(agent.address.address, agent.address.city.name, agent.address.city.state.name, agent.address.zip.code) }
        result = requests.get(url,params)

        result_json = result.json()

        agent.address.latitude =result_json['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude'] if result_json['Response'] else 0
        agent.address.longitude = result_json['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude'] if result_json['Response'] else 0

        agent.address.save()
        time.sleep(1)

        print (agent.address.latitude,agent.address.longitude)

        return
    except Exception as e:
        print (e)



#calculate between agents and main states

from .models.stateDistance import Distance
from geopy.distance import great_circle
from decimal import Decimal
def calculateDistance(request):
    states = RootState.objects.all()
    agents = Agent.objects.all()
    try:
        for state in states:
            for agent in agents:
                d = getDistance(state.id,agent.id)
                dis = Distance.objects.create(
                agent=agent,
                source=state,
                distance=d
                )
                dis.save()

        return JsonResponse({'message':"Distance between agents and states completed"})
    except Exception as e:
        print (e)

def getDistance(state_id,agent_id):
    agent = Agent.objects.get(id=agent_id)
    state = RootState.objects.get(id=state_id)

    source = (state.latitude,state.longitude)


    destination= (agent.address.latitude,agent.address.longitude)


    return round(great_circle(source, destination).km,2)



#displays the nearest agents for each state

def nearestAgents(request,id):
    instance = get_object_or_404(RootState,id=id)
    d = Distance.objects.filter(source=instance).order_by('distance')[:100]
    states = RootState.objects.all()
    context={"data":d,"states":states,"instance":instance}
    return render(request,"nearest_agents.html",context)

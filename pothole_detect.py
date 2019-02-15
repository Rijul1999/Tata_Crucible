"""
This is the code file for detection of potholes on the roads of India. We use the gmaps.js library to implement our algorithm on the Google Maps API

"""
api_key = "3OC08f7c9ad7s9tutturu7v07sdv666"
import gmaps
#configure api
gmaps.configure(api_key=api_key)
#Define location 1 and 2
Durango = (37.2753,-107.880067)
SF = (37.7749,-122.419416)
#Create the map
fig = gmaps.figure()
#create the layer
layer = gmaps.directions.Directions(Durango, SF,mode='car')
#Add the layer
fig.add_layer(layer)

from datetime import datetime

now =  datetime.now()
directions_result = gmaps.directions("37.2593, -107.3490", mode="driving", avoid="potholes", departure_time="now")



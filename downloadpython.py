import os
import requests

print ("Hello World")
path = os.getcwd()
print(path)
print (os.listdir())
print(type(path))
response = requests.get ('http://172.18.0.3:8081/repository/micro-integrator/MP-FavouriteRoute/MP-FavouriteRoute-CAR/1.0.0/MP-FavouriteRoute-CAR-1.0.0.zip')
print(response)

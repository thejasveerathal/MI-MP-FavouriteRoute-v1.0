import requests
import os
from pathlib import Path

print('Download Starting...')
 
url = 'http://172.18.0.3:8081/repository/micro-integrator/MP-FavouriteRoute/MP-FavouriteRoute-CAR/1.0.0/MP-FavouriteRoute-CAR-1.0.0.zip'
p = Path(url)

artifact = p.name


req = requests.get(url, stream=True)
 
 
with open(p.name,'wb') as output_file:
    for chunk in req.iter_content(chunk_size=1025):
        if chunk:
            output_file.write(chunk)

print('Download Completed...')            
 
os.rename(artifact,artifact.replace("zip","car")) 

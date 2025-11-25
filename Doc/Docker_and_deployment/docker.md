##### Build docker
```
docker build -f Dockerfile.dev -t simplegemini-dev .
```
##### Check docker image
<code>docker images</code>
##### Access to docker
<code>docker run -it --name fastapi-dev-container -p 8000:8000 -v %cd%:/code fastapi-dev bash</code>
or
```
docker run -it --name simplegemini-dev-container -p 8000:8000 -e GOOGLE_API_KEY="AIzaSy...Nvg" -v %cd%:/code simplegemini-dev bash


import os
os.getenv("GOOGLE_API_KEY")
>>> 'AIzaSy...Nvg'
```
##### Stop and remove container
<code>docker stop fastapi-dev-container</code>
<code>docker rm fastapi-dev-container</code>

##### Enter container later
<code>docker exec -it fastapi-dev-container bash</code>

##### Find ID of docker that running
<code>docker ps</code>

##### Stop docker that running
<code>docker stop (container_id)</code>

##### Remove it
<code>docker rm (container_id)</code>

##### Run your container with PORT MAPPING\
docker run -it --name simpleapi-dev-container  -p 4000:4000  -v %cd%:/code simpleapi-dev bash

##### Build docker
<code>docker build -f Dockerfile.dev -t fastapi-dev .</code>

##### Check docker image
<code>docker images</code>
##### Access to docker
<code>docker run -it --name fastapi-dev-container -p 8000:8000 -v %cd%:/code fastapi-dev bash</code>

##### Stop and remove container
<code>docker stop fastapi-dev-container</code>
<code>docker rm fastapi-dev-container</code>

##### Enter container later
<code>docker exec -it fastapi-dev-container bash</code>

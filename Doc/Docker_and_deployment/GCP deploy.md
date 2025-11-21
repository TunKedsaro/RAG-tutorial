##### build docker
<code>docker build -f Dockerfile.dev -t fastapi-dev .</code>

##### Exec in to docker machine
<code>docker run -it --name fastapi-dev-container -p 8000:8000 -v %cd%:/code fastapi-dev bash</code>

##### gcloud init
<code>root@a5c0521d7985:/code# gcloud init</code>
<code>>>>[30] cs-poc-6ybmdro11muhuzqa0ti4uuj</code>
<code>>>>[30] asia-southeast1-a</code>

<code>root@a5c0521d7985:/code# gcloud artifacts repositories create custom-fastapi \<br>
  --repository-format=docker \<br>
  --project=cs-poc-6ybmdro11muhuzqa0ti4uuj \<br>
  --location=asia-southeast1
  </code>
  

<code>root@a5c0521d7985:/code# gcloud builds submit \<br>
  --config=cloudbuild.yaml \<br>
  --project=cs-poc-6ybmdro11muhuzqa0ti4uuj
  </code>


##### Create service.yaml
<code>root@a5c0521d7985:/code# echo "" > service.yaml</code>


<code>
root@a5c0521d7985:/code# gcloud run services replace service.yaml \<br>
    --region asia-southeast1 \<br>
    --project cs-poc-6ybmdro11muhuzqa0ti4uuj
</code>


<code>root@a5c0521d7985:/code# gcloud run services set-iam-policy custom-fastapi-service     gcr-service-policy.yaml<br>     
--region=asia-southeast1<br>    
--project=cs-poc-6ybmdro11muhuzqa0ti4uuj<br>
</code>


##### Deploy
<code>
root@a5c0521d7985:/code# PROJECT_ID="cs-poc-6ybmdro11muhuzqa0ti4uuj"
REGION="asia-southeast1"
REPO="custom-fastapi"

gcloud run deploy custom-fastapi-service \ <br>
  --image="$REGION-docker.pkg.dev/$PROJECT_ID/$REPO/custom-fastapi:latest" \      <br>   
  --region="$REGION" \ <br>
  --memory=2Gi \ <br>
  --cpu=2 \ <br>
  --max-instances=5 \ <br>
  --set-env-vars APP_ENV=prod <br>
  </code>
##### Test it
<code>root@a5c0521d7985:/code# gcloud run services describe custom-fastapi-service \    <br>  
    --region asia-southeast1 \ <br>
    --project cs-poc-6ybmdro11muhuzqa0ti4uuj \ <br>
    --format 'value(status.url)' <br>
</code>

<code>
root@a5c0521d7985:/code# curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" \<br>
     https://custom-fastapi-service-qpfpb3rvma-as.a.run.app
</code>
##### Output
<code>>>> {"message":"OK 🚀"}root@a5c0521d7985:/code#</code>


##### Get token for Postman
<code>root@a5c0521d7985:/code# gcloud auth print-identity-token</code>
<code>>>> eyJhbGciOiJSUzI1NiIsImtpZCI6ImE1NzMzYmJiZDgxOGFhNWRiMTk1MTk5Y2Q1NjhlNWQ2ODUxMzJkM2YiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIzMjU1NTk0MDU1OS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjMyNTU1OTQwNTU5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTE3ODE4ODEyODIzMTc4NjQ5NjM3IiwiZW1haWwiOiJ0dW4ua0B0ZXJyYWRpZ2l0YWx2ZW50dXJlcy5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IjZUSDBfZWVlREpTdXRlNXRRT2U4M2ciLCJpYXQiOjE3NjM2MjQ1ODAsImV4cCI6MTc2MzYyODE4MH0.G63sO23KyesT6jzv7vV4FV6KPTJCt5oWgSF_POUYYu6YHtjwuQudThR4QF9YzAc9Io-sXG1c_K7jFQ2ZlPuSbRK9enibTWZxg5o3FbamI113Fi5kp5x81EsP1dQVEsnm0kdP5_mEtWK9X8vWAaUxCl-JCYP5gJ_fHB0E49fLizgVtgWyJ5NHhu3pHQl6SN1AmlxsWdp84AdBDANEgpGeqkVJrqT1F6K2uBckTffG2t0fqOQ9aE0qzg8JsllWUkqyUSQpEZf6Fk0DiKbsKdieD7E4uw3B3rgMG4Ct51iifr8a2qBFr1s_vlPyPykG3KY_kmbi3p6RkwG2z6v7qQvBvQ</code>


![[Pasted image 20251120155421.png]]
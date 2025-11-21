
C:\Users\TunKedsaro\Desktop\how-to-deploy-a-dockerized-fastapi-to-google-cloud-run>docker build -f Dockerfile.dev -t fastapi-dev .
[+] Building 159.1s (10/10) FINISHED                       docker:desktop-linux
 => [internal] load build definition from Dockerfile.dev                   0.1s
 => => transferring dockerfile: 602B                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim        0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => CACHED [1/6] FROM docker.io/library/python:3.12-slim                   0.0s
 => [2/6] RUN apt-get update && apt-get install -y apt-transport-https c  20.0s
 => [3/6] RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg   0.8s
 => [4/6] RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg]   0.6s
 => [5/6] RUN apt-get update && apt-get install -y git vim net-tools bu  111.0s
 => [6/6] WORKDIR /code                                                    0.1s
 => exporting to image                                                    26.3s 
 => => exporting layers                                                   26.2s 
 => => writing image sha256:5bdca6fe4cf0b1c537db495298c6857b80804b1914a02  0.0s 
 => => naming to docker.io/library/fastapi-dev                             0.0s 

C:\Users\TunKedsaro\Desktop\how-to-deploy-a-dockerized-fastapi-to-google-cloud-run>docker run -it --name fastapi-dev-container -p 8000:8000 -v %cd%:/code fastapi-dev bash
root@837bf137ff3b:/code# gcloud --version
Google Cloud SDK 473.0.0
alpha 2024.04.19
beta 2024.04.19
bq 2.1.4
bundled-python3-unix 3.11.8
core 2024.04.19
gcloud-crc32c 1.0.0
gsutil 5.27
root@837bf137ff3b:/code# gcloud init
Welcome! This command will take you through the configuration of gcloud.        

Your current configuration has been set to: [default]

You can skip diagnostics next time by using the following flag:
  gcloud init --skip-diagnostics

Network diagnostic detects and fixes local network connection issues.
Checking network connection...done.
Reachability Check passed.
Network diagnostic passed (1/1 checks passed).

You must log in to continue. Would you like to log in (Y/n)?  y

Go to the following link in your browser, and complete the sign-in prompts:

    https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=32555940559.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fsdk.cloud.google.com%2Fauthcode.html&scope=openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fappengine.admin+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fsqlservice.login+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcompute+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Faccounts.reauth&state=1lAxs7ccvCvYWYMK3qNC4X5Dn6guSj&prompt=consent&token_usage=remote&access_type=offline&code_challenge=LkIvFFlxn5unLw3W5CzjMgoLdxWMrUxpUTp7ElwA97c&code_challenge_method=S256

Once finished, enter the verification code provided in your browser: 4/0Ab32j935PtldkG9Shp252WbWj_wYs8wNnjtvlq446Ej_mSRZ_22kJ-6AKte4GdEf7syFkg
You are logged in as: [tun.k@terradigitalventures.com].

Pick cloud project to use: 
 [1] aip-automation-artifact
 [2] aip-automation-bootstrap
 [3] aip-automation-ci-cd
 [4] aip-dev-ai
 [5] aip-dev-application
 [6] aip-dev-data
 [7] aip-dev-external
 [8] aip-lz-billing
 [9] aip-lz-iam
 [10] aip-lz-networking
 [11] aip-lz-remote-access
 [12] aip-lz-security
 [13] aip-prd-ai
 [14] aip-prd-application
 [15] aip-prd-data
 [16] aip-prd-external
 [17] aip-preprd-ai
 [18] aip-preprd-application
 [19] aip-preprd-data
 [20] aip-preprd-external
 [21] aip-sit-ai
 [22] aip-sit-application
 [23] aip-sit-data
 [24] aip-sit-external
 [25] aip-uat-ai
 [26] aip-uat-application
 [27] aip-uat-data
 [28] aip-uat-external
 [29] cs-host-fb9f74f99c984bb8bbc5f1
 [30] cs-poc-6ybmdro11muhuzqa0ti4uuj
 [31] cvevaluation-01
 [32] gen-lang-client-0156389874
 [33] google-mpf-532040072629
 [34] green-rookery-455408-d5
 [35] hi-lab-projects
 [36] llrs-prod
 [37] ndlp-poc
 [38] poc-piloturl-nonprod
 [39] poc-plagiarism
 [40] poc-project-471710
 [41] poc-sitetestcheck-nonprod
 [42] poc-skytestdomain-nonprod
 [43] prj-b-cicd-wif-gh-90e9
 [44] prj-b-seed-b0a7
 [45] prj-c-billing-export-x46u
 [46] prj-c-kms-4mk3
 [47] prj-c-logging-kjb0
 [48] prj-c-scc-byry
 [49] prj-c-secrets-f5ln
 [50] prj-d-bu1-sample-base-b39r
Did not print [92] options.
Too many options [142]. Enter "list" at prompt to print choices fully.
Please enter numeric choice or text value (must exactly match list item):  31   

Your current project has been set to: [cvevaluation-01].

Not setting default zone/region (this feature makes it easier to use
[gcloud compute] by setting an appropriate default value for the
--zone and --region flag).
See https://cloud.google.com/compute/docs/gcloud-compute section on how to set  
default compute region and zone manually. If you would like [gcloud init] to be 
able to do this for you the next time you run it, make sure the
Compute Engine API is enabled for your project on the
https://console.developers.google.com/apis page.

Created a default .boto configuration file at [/root/.boto]. See this file and  
[https://cloud.google.com/storage/docs/gsutil/commands/config] for more
information about configuring Google Cloud Storage.
Your Google Cloud SDK is configured and ready to use!

* Commands that require authentication will use tun.k@terradigitalventures.com by default
* Commands will reference project `cvevaluation-01` by default
Run `gcloud help config` to learn how to change individual settings

This gcloud configuration is called [default]. You can create additional configurations if you work with multiple accounts and/or projects.
Run `gcloud topic configurations` to learn more.

Some things to try next:

* Run `gcloud --help` to see the Cloud Platform services you can interact with. And run `gcloud help COMMAND` to get help on any gcloud command.
* Run `gcloud topic --help` to learn about advanced features of the SDK like arg files and output formatting
* Run `gcloud cheat-sheet` to see a roster of go-to `gcloud` commands.
root@837bf137ff3b:/code#




![[Pasted image 20251120105449.png]]
![[Pasted image 20251120105525.png]]
![[Pasted image 20251120105551.png]]
![[Pasted image 20251120105621.png]]gcloud artifacts repositories create custom-fastapi \
  --repository-format=docker \
  --project=cs-poc-6ybmdro11muhuzqa0ti4uuj \
  --location=asia-southeast1

![[Pasted image 20251120133716.png]]

steps:

  - name: 'gcr.io/cloud-builders/docker'

    args: [

      'build',

      '-f', 'Dockerfile.prod',

      '-t', 'asia-southeast1-docker.pkg.dev/cs-poc-6ybmdro11muhuzqa0ti4uuj/custom-fastapi/custom-fastapi:latest',

      '.'

    ]

  

  - name: 'gcr.io/cloud-builders/docker'

    args: [

      'push',

      'asia-southeast1-docker.pkg.dev/cs-poc-6ybmdro11muhuzqa0ti4uuj/custom-fastapi/custom-fastapi:latest'

    ]





====================================
gcloud builds submit \
  --config=cloudbuild.yaml \
  --project=cs-poc-6ybmdro11muhuzqa0ti4uuj


gcloud run services replace service.yaml \
    --region asia-southeast1


=====================================
gcloud run services replace service.yaml \
  --region asia-southeast1 \
  --project cs-poc-6ybmdro11muhuzqa0ti4uuj




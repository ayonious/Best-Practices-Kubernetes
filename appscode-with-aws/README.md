#Kubernetes Installation in appscode (creting the cluster in aws)



## 1. install appctl:

Try from this page:
https://appscode.com/cli/get/appctl/


after installing you have to login:
```
appctl login
Team Name: XXXX
# you can find your teamname in the url of appscode
# lookinthe url <temname>.appscode.io
```
This outputs a url from which you are supposed to copy the token and paste in the comand line

after that you are logged in into appscode

```
Paste the token here:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Do you want to help improve AppsCode by collecting cli usage information? (Y/n): n
Login successful.
```


## 2. create user in aws and let appscode become this user

Create a user in aws. Give it permission of 

1. read EC2 containers 
2. access S3
3. access EC2
(lazy people just give it admin permission :P)


Now in appscode>pharm>credentials>put your key created in aws

## 3. configure aws in your local pc and create secret.yml

```
aws configure
```
use the credentials you just created in aws



now get auth token:
```
aws ecr get-login --region=XX-XXXX-X
#paste whatever you got in the console and enter
```


now create secret with this(for more info read aws/installation):
```
cat ~/.docker/config.json | base64
```


## 4. Create the cluster:

pharm>cluster>create cluster>select configs>create>wait few minutes>its done


## 5. start using appctl cli

List all the created clusters:
```
appctl cluster list
```

Now change your kubernetes cluster namespace to appscode cluster:
```
appctl cluster use XXXXXXXX
```

make sure docker daemon is running (this command should work):
```
docker images
```


See all the namespaces in kubectl
```
kubectl get namespaces
```


ssh into a node:
```
appctl cluster ssh -c <cluster_name> <ip-XXX-XX-X-XXX.XXX.internal>
```



#Minikube practice

##Prereq
Install kubernetes from kubernetes/installation.md

##Installation
For latest version installation see: https://github.com/kubernetes/minikube/releases

Quick installation steps:
  1. Download the latest binary from `https://github.com/kubernetes/minikube/releases`
  2. Now just make the binary executable `chmod +x minikube-darwin-amd64`
  3. and then put it in `bin` folder  `cp minikube-darwin-amd64 /usr/local/bin/`

#Configure k8s with minikube:

Simply run this:
>```
>minikube start
>```
>Output:
>```
>Starting local Kubernetes cluster...
>Kubectl is now configured to use the cluster.
>```


See if minikube is configured in kubernetes:
>```
>kubectl config view
>```
>Output
>```
>apiVersion: v1
>clusters:
>- cluster:
>    certificate-authority: /Users/<username>/.minikube/ca.crt
>    server: https://XXXXXXX:XXXX
>  name: minikube
>contexts:
>- context:
>    cluster: minikube
>    user: minikube
>  name: minikube
>current-context: minikube
>kind: Config
>preferences: {}
>users:
>- name: minikube
>  user:
>    client-certificate: XXXX/.minikube/apiserver.crt
>    client-key: XXXX/.minikube/apiserver.key
>```

################################
RUN ALL YOUR KUBERNETES COMMANDS
################################

#Getting external url for a service:
```
minikube service hello-minikube --url
```



#Remvoe the cluster:
```
minikube stop
```


	
## Creating your docker hub

You need a docker hub in case you are thinking about having some free docker images on which you can test you local kubernetes cluster. In the examples used here I have pushed the images in my private docker repo, and the repo is public so anyone can pull but only I can push.


## How to create your own docker hub

	1. Register here: `https://cloud.docker.com`
	2. Create a new repository where you can push the images
	3. `docker login` use your credentials to login and then push everything
	4. now I can push stuffs using `docker push docker.io/ayonnayihan/sample-image-test:0.1`


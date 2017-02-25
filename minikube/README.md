#Minikube practice

##Prereq
Install kubernetes from kubernetes/installation.md

##Installation
For latest version installation see: https://github.com/kubernetes/minikube/releases


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
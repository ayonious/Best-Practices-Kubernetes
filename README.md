#Kubernetes

Kubernetes (commonly referred to as "k8s") is an open source container cluster manager originally designed by Google and donated to the Cloud Native Computing Foundation. It aims to provide a "platform for automating deployment, scaling, and operations of application containers across clusters of hosts".

Kubernets is an orchestrator that runs docker containers. User installs kubernets in his local computer and runs the cloud from his local machine. The cluster that kubernetes creates can be in aws/google/other

There are 3 folders that describes procedure to create the cluster in different cluster providers

In this project we are going to leart how to use Kubernetes (k8s) and creating the cluster in different providers:

`Commonfiles` contains all the common installation instructions for installing k8s in your local pc

It also contains instructions for creating the cluster in these:

	1. aws
	2. appscode
	3. minikube


# Synopsys

## Installing kubernetes:
===============================================
Find the latest version here:
```
https://github.com/kubernetes/kubernetes/releases
```

Then goto changelog and find the proper client version for me its `darwin 64amd` just download it, extract it
```
cd platforms/darwin/amd64
chmod +x kubectl
cp kubectl /usr/local/bin/kubectl
kubectl version
```


## Another way of installing kubernetes:
=========================================
For Mac installing the latest version:
```
brew install kubernetes-cli
```

If the above command fails because of previous installation you might need to run this to overrite with this installation
```
brew link --overwrite kubernetes-cli
```

To Check that kubectl is properly configured(and remote cluster is reachable) by getting the cluster state:
```
kubectl cluster-info
```
If you see a url response, you are ready to go.



	
## Creating your docker hub

You need a docker hub in case you are thinking about having some free docker images on which you can test you local kubernetes cluster. In the examples used here I have pushed the images in my private docker repo, and the repo is public so anyone can pull but only I can push.


## How to create your own docker hub

	1. Register here: `https://cloud.docker.com`
	2. Create a new repository where you can push the images
	3. `docker login` use your credentials to login and then push everything
	4. now I can push stuffs using `docker push docker.io/ayonnayihan/sample-image-test:0.1`


## Cheatsheet
```
kubectl get version

kubectl get nodes
kubectl get pods
kubectl get secrets
kubectl get services
kubectl create -f <file>
kubectl get namespaces
kubectl logs <pod-name> 
kubectl port-forward <pod-name> <local-port>:<remote-port>

kubectl delete pods --all

kubectl exec <pod-name> -- ls /                         # Run command in existing pod (1 container case)
kubectl exec <pod-name> -c <container-name> -- ls /     # Run command in existing pod (multi-container case)

kubectl config view
kubectl cluster-info
```

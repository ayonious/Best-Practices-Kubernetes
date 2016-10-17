#Kubernetes Installation


## Official way to installing kubernetes:
===============================================
Find the latest version here:
```
https://github.com/kubernetes/kubernetes/releases
```
just download it, extract it, inside goto platforms folder and find peoper version for your usage. This is a prebuild release so you can simply add in in someplace and start using it.

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

Check that kubectl is properly configured by getting the cluster state:
```
kubectl cluster-info
```
If you see a url response, you are ready to go.


#Kubernetes Installation


## Official way to installing kubernetes:
===============================================
Find the latest version here:
```
https://github.com/kubernetes/kubernetes/releases
```

Then goto changelog and find the proper client version for me its `darwin 64amd`

just download it, extract it

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


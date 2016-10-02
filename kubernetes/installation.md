#Kubernetes Installation

Check that your system supports VT-x/AMD-v virtualization by running this command:
```
sysctl -a | grep machdep.cpu.features | grep VMX
```
My output is something like this
```
machdep.cpu.features: XXX XXX XXX XXXXX XXXX XXXX XXXXXX XXX XXX XXXXX XXXX XXXX XXXXXX XXX XXX XXXXX XXXX XXXX XXXXXX XXX XXX XXXXX XXXX XXXX XXXXXX XXX XXX XXXXX XXXX XXXX XXX
```

Now install Kubernetes (make sure to install the latest version, here were going to install v1.3.6):
```
curl -Lo kubectl http://storage.googleapis.com/kubernetes-release/release/v1.3.6/bin/darwin/amd64/kubectl && chmod +x kubectl && sudo mv kubectl /usr/local/bin/
```

For Mac installing the latest version:
```
brew install kubernetes-cli
```

if the above command fails because of previous installation you might need to run this to overrite with this installation
```
brew link --overwrite kubernetes-cli
```


Check that kubectl is properly configured by getting the cluster state:
```
kubectl cluster-info
```
If you see a url response, you are ready to go.

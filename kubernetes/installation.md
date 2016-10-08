#Kubernetes Installation

Check that your system supports VT-x/AMD-v virtualization by running this command:
```
sysctl -a | grep machdep.cpu.features | grep VMX
```
My output is something like this
```
machdep.cpu.features: XXX XXX XXX XXXXX XXXX XXXX XXXXXX XXX XXX XXXXX XXXX XXXX XXXXXX XXX XXX XXXXX XXXX XXXX XXXXXX XXX XXX XXXXX XXXX XXXX XXXXXX XXX XXX XXXXX XXXX XXXX XXX
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

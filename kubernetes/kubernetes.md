#Kubernetes Running Commands



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


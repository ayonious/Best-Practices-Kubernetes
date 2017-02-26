# Minikube practice project



### Build the image:
	docker build -t docker.io/ayonnayihan/sample-image-test:0.12 .
### See list of images built and see that youre image is there
	docker images
### Push the images to dockerhub (hope you have permission only I can push and I have already done that so you can just download and use from anywhere)
```
	# to get push permission `docker login`
	docker push docker.io/ayonnayihan/sample-image-test:0.12 
```
### now create the rc and monitor it
```
	kubectl create -f ayonAppServer-rc.yaml
	kubectl get pods
	kubectl get rc
	kubectl cluster-info
	kubectl describe pods <pod-id>
	kubectl logs <pod-id>
```


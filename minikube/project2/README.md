# Minikube practice project2


## Run using python script
```
#console1
cd receiverContainer
python script.py "localhost" "5555"

#console2
cd senderContainer
python script.py "localhost" "5555"
```


## Run using docker

```
#console1
cd receiverContainer
docker build -t docker.io/ayonnayihan/sample-sendr-rcv-test:receiver0.1 .
docker push docker.io/ayonnayihan/sample-sendr-rcv-test:receiver0.1

#console2
cd senderContainer
docker build -t docker.io/ayonnayihan/sample-sendr-rcv-test:sender0.1 .
docker push docker.io/ayonnayihan/sample-sendr-rcv-test:sender0.1 .
```



### 1. Run using docker network creating
```
#Console1
docker run  --name="testListen" --env LISTEN_HOST="0.0.0.0" --env LISTEN_PORT="5555" --network=sample-sendr-rcv-test -d docker.io/ayonnayihan/sample-sendr-rcv-test:receiver0.1

#Console2
docker run --name="testTalk" --env SEND_HOST="testListen" --env SEND_PORT="5555" --network=sample-sendr-rcv-test -d docker.io/ayonnayihan/sample-sendr-rcv-test:sender0.1
```

### 2. Run using docker compose
```
See the file `docker-compose.yml`
docker-compose build
```

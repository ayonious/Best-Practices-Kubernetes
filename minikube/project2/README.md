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

## Run using docker run
```
#console1
cd receiverContainer
docker build -t docker.io/ayonnayihan/sample-sendr-rcv-test:receiver0.1 .

docker run --name="testListen" -p 5555:5555 --env LISTEN_HOST="localhost" --env LISTEN_PORT="5555" docker.io/ayonnayihan/sample-sendr-rcv-test:receiver0.1


#console2
cd senderContainer
docker build -t docker.io/ayonnayihan/sample-sendr-rcv-test:sender0.1 .

docker run --name="testTalk" --env SEND_HOST="localhost" --env SEND_PORT="5555" docker.io/ayonnayihan/sample-sendr-rcv-test:sender0.1
```





#Configure your kubernete to work with aws


## 1. Install aws-cli


Linux:
```
sudo apt-get install python2.7;
curl -O https://bootstrap.pypa.io/get-pip.py;
sudo python get-pip.py;
sudo pip install awscli;
```
OSX: (I installed version: awscli-1.10.61.el_capitan )
```
brew install python
brew install awscli
```


## 2. Create a User in AWS

Create a user in aws web. Give it permission to make changes as admin


## 3. Configure aws

Now you need to configure AWS in your pc so that all the commands aws will run, it will be run as the user you just created

```
aws configure
AWS Access Key ID [*************]: WRITE YOUR ACCESS KEY OF THE USER YOU CREATED
AWS Secret Access Key [*********]: YOU CAN DOWNLOAD THIS KEY 1 TIME WHEN YOU CREATE THE USER IN AWS
Default region name [XX-XXXX-XX]: write you region name like us-east-1
Default output format [None]: you can just enter here, enter will keep the default val
```

## 4. Configure Kubernetes to use AWS cloud (make sure you put proper version numbers)

First create a directory suppose 'myproject'. Now download v1.3.4 careful about this 1.3.5,1.3.6 has problems with aws kube-up.sh
```
cd myproject
export K8S_VERSION=v1.3.4; curl -SLO https://github.com/kubernetes/kubernetes/releases/download/$K8S_VERSION/kubernetes.tar.gz
tar xzvf kubernetes.tar.gz
vi bootstrap-cluster.sh
```

now put these in this file:
```
#!/bin/bash

export KUBERNETES_PROVIDER=aws
export KUBE_AWS_ZONE=XX-XXXX-XX
export MASTER_SIZE=m3.medium
export NODE_SIZE=t2.small
export NUM_NODES=1
export AWS_SSH_KEY=$HOME/.ssh/id_rsa

function cluster_up {
   ./kubernetes/cluster/kube-up.sh
}

function cluster_down {
   ./kubernetes/cluster/kube-down.sh
}

if [[ "${1:-up}" == "down" ]]; then
   cluster_down
else
   cluster_up
fi
```

configure the master and node things and then bring the cluster up by:
>```
>./bootstrap-cluster.sh cluster_up
>```
>
>```
>... Starting cluster using provider: aws
>... calling verify-prereqs
>... calling kube-up
>Starting cluster using os distro: vivid
>Uploading to Amazon S3
>```


################################
RUN ALL YOUR KUBERNETES COMMANDS
################################


#Remvoe the cluster:
```
./bootstrap-cluster.sh cluster_down
```


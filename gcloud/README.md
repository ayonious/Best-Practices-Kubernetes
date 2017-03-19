## Install gcloud
curl https://sdk.cloud.google.com | bash

In case the installation didn’t work out:
This will download cloud and put in somewhere in ~/ folder
You need to add the path to this folder in your env variable to start using the command ‘gcloud'

I used this solution and it worked
http://stackoverflow.com/questions/25468074/get-fish-shell-to-work-with-gcloud-command-line-tools

But in my other Mac I didn’t need any of these hacks to install cloud


## Loginto gcloud with your google account

```
gcloud auth login
```
this will open the browser and you have to give permission to access to particular account that is used with your console.google account


See list of all account in your client
```
gcloud auth list
```

## To connect with remote gcloud custer


1. Goto `https://console.cloud.google.com`
2. Container engine >  Contianer clusters
3. You will see list of all clusters there
4. Find the `connect` button that will show you the comman to configure your kubernetes client with this cluster

Its usually something like this:
```
gcloud container clusters get-credentials <projname> \
    --zone <zone-name> --project <project-name>
```










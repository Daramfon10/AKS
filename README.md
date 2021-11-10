# Deploying an Image from Azure Container Registry to AKS
## Prerequisites
 1. Create an Azure Container Registry
 2. Create a service principal so AKS can use it to access your container registry.
 3. Push your image to Azure Container Registry

## Overview

- The **podconfig.YAML** file contains the configuration for a single pod. For this instance, the pod is configured with two **Nvidia pytorch containers** with each container mounted with [Volumes](https://docs.microsoft.com/en-us/azure/aks/concepts-storage) - persistent volumes and configMaps.
- The pods are also configured to run the python script that has been injected into the container using configmaps.

## Steps

1. Clone the repository - `git clone https://github.com/Daramfon10/AKS.git`
2. Change directory to the cloned repository - `cd AKS`
3. Create an image pull secret for Kubernetes to store information needed to authenticate your registry - `kubectl create secret docker-registry <secret-name> \
    --docker-server=<REGISTRY_NAME>.azurecr.io \
    --docker-username=<Service principal appId> \
    --docker-password=<Service principal password>`
4. Open the podconfig.YAML file - `.\podconfig.YAML`
5. Update the following fields:
   -  The pod name with a name of your choice
   -  The image name for each container, replace the <Registry Name> portion with your registry name. Make sure you tagged the **Nvidia pytorch image** right. Example with a registry name of **testacr** the expected image name would be **testacr.azurecr.io/nvcr.io/nvidia/pytorch:v21.09**
   - The secret name should be updated with the name for the secret created in **step 3**
6. 
```

```


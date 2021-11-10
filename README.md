# Running Jobs on AKS Cluster, Utilizing ConfigMaps and Dynamic Persistent Volumes
## Prerequisites
 1. Create an Azure Container Registry
 2. Create a service principal so AKS can use it to access your container registry.
 3. Push your image to Azure Container Registry
 4. Create an AKS cluster

## Overview

- The **podconfig.YAML** file contains the configuration for a single pod. For this instance, the pod is configured with two **Nvidia pytorch containers** , each container is mounted with [Volumes](https://docs.microsoft.com/en-us/azure/aks/concepts-storage) - persistent volumes and configMaps.
- The pods are also configured to run the **python script** that has been injected into the container using **configmaps and produce output files that are stored in a storage account.**

## Environment Setup using Azure CLI
1. Install [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli). 
2. To connect to the Kubernetes cluster from your local computer, install the kubernetes cli - `az aks install-cli`
3. Connect to your cluster - `az aks get-credentials --resource-group myResourceGroup --name myAKSCluster`
4. To verify that connection is complete, check the list of nodes running in the cluster - `kubectl get nodes`

## Creating Resources in the Cluster

For this exercise we will need to create configMap, storageclass and persistent volume resources in the cluster using our customized files. The steps below give a walkthrough on how to create these resources:
1. Clone the repository - `git clone https://github.com/Daramfon10/AKS.git`
2. Change directory to the input files directory in the cloned repository - `cd AKS/input-files`
3. Create the configMap resource from two files - `kubectl create configmap input --from-file jon.json --from-file script.py`
4. Change directory to the volume directory - `cd ..\volumes\`
5. Create the storage class resource - `kubectl create -f storageclass.YAML`
6. Create the persistent volume resource with the storage class provisioned to it - `kubectl create -f pv.YAML`

## Setting Up the Pod Configuration File

Now that we have all our resources in the cluster, we need to make sure we have the **podconfig.YAML** file configured properly before we run the file.
1. Change directory to the home directory in the clone repository - `cd ..`
2. Login to your Azure container registry - `az acr login --name <Registry Name>`
3. Create an image pull secret for Kubernetes to store information needed to authenticate your registry - `kubectl create secret docker-registry <secret-name> \
    --docker-server=<REGISTRY_NAME>.azurecr.io \
    --docker-username=<Service principal appId> \
    --docker-password=<Service principal password>`
3. Open the podconfig.YAML file - `.\podconfig.YAML`
4. Update the following fields:
   -  The pod name with a name of your choice
   -  The image name for each container, replace the <Registry Name> portion with your registry name. Make sure you tagged the **Nvidia pytorch image** right. Example with a registry name of **testacr** the expected image name would be **testacr.azurecr.io/nvcr.io/nvidia/pytorch:v21.09**
   - The secret name should be updated with the name for the secret created in **step 3**
5. Save the file.
 
 ## Creating a Pod Resource
 
 We can now proceed to creating a pod resource using the **podconfig.YAML** file.
 1. Create the pod resource - `kubectl create -f podconfig.YAML`
 2. Verify that the pod has been created - `kubectl get pods`
    - The output from this should show a list of pods that you have created. If your **pod was successfully created** you should have the pod name with status of running (2/2) containers. 
    - In the case there are any errors, to help debug run the command - `kubectl describe pod <Name of Pod>`
 
 ## Verification
 
 The following steps helps verify that our pod was configured properly with the configMap and persistent volume mounted in the containers and the script executed once the containers have been created:
 1. Launch the containers in interactive mode by running - `kubectl exec -it <Pod Name> /bin/bash`
 2. While inside the container, verify that the configMap was mounted in the container. There should be two input files (**jon.json & script.py**) - `ls inputfiles/`
 3. List the files in the store folder to verify that **script.py** was executed properly. There should be **three output files** in the store directory - `ls store/`
 4. To verify that the output files are stored in a storage account:
    - Login to the [Azure Portal](portal.azure.com)
    - Click on resource groups
    - With your subscription filtered, search for a resource group that begins with *MC_myResourceGroup_myAKSCluster_* .This contains all of the infrastructure resources associated with the cluster.
    - In the resources list for the resource group, select the storage item of storage account type. 
    - In the pane on the left, click on **File Share** to see the persistent volume. Click on the persistent volume to open.
    - You should have the same 3 output files in step 3 inside this folder. This means that you have successfully claimed a persistent volume for your pod.

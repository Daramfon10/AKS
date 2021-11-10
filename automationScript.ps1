#loops until condition is no longer met and then calls the python script each time. The python script makes modifications to the YAML file - The pod name is changed. Once that is complete then the pod is created using the create command.
for ($num = 1 ; $num -le 2 ; $num++) {
    py C:/Users/dakpan/Desktop/podshuffle.py
    kubectl create -f C:/Users/dakpan/Desktop/podconfig.yaml
}
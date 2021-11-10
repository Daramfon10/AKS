import random
import os
""" 
Use Alt + Shift + A for this comment block 

Approach: 
- The python file will take the input of number of pods to create. 
- Then open the config YAML file and then edit the pod name to have a different number of pods.
- close the file and save it 
"""



podconfigPath = "C:/Users/dakpan/Desktop/podconfig.yaml"
podNumber = random.randint(1,100)

def Tester(f):
    
    for line in f:
        print(line)
#O(L)
def handler():
    file = open(podconfigPath, "r")
    lineToReplace = ""
    for line in file:
        if "name" in line:
            lineToReplace = line
            break
    file.close()
    #print(lineToReplace,podNumber)

    newf = open(podconfigPath, "r")
    data = newf.read()
    replacedText = "  name: dara-pod" + str(podNumber) + "\n"
    data = data.replace(lineToReplace, replacedText)
    newf = open(podconfigPath,"w")
    newf.write(data)
    newf.close()
    #newf = open(podconfigPath,"r")
    #Tester(newf)   

handler()
#inputFileHandler()
#print("Hello World")
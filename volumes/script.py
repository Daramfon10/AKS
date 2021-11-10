import json
import os
#open Json file that was shared and load the data into a variable called "data"
"""
Approach:
- load the JSON file that was shared and load the data into a variable called "data"
- loop through the data dictionary and for each key then loop into the list value.
- Then multiply and also add the values of all the items in the list and store them into variables.
- create a file in the preferred directory in the container to store the multiplication and addition output of each key. 
- The file name will have the key appended to it.
- Write the multiply and addition values for each key into the files created for each key

Jon's request: Store the data as a JSON file. Nomenclature of the output file name is good using dates, metadata...etc.

Pod -> PVC -> PV -> Storage
"""
with open("/workspace/inputfiles/jon.json") as jdata:
    data = json.load(jdata)
print("data: {}".format(data))

for key in data:
    multiplyOutput = 1
    additionOutput = 0
    for valueItem in range(0,len(data[key])):
        multiplyOutput *= int(data[key][valueItem])
        additionOutput += int(data[key][valueItem])
    finalMultiplyOutput = "multiplicationOutput:" + str(multiplyOutput)
    finalAdditionOutput = "additionOutput:" + str(additionOutput)
    hostName = os.getenv('HOSTNAME')
    output = "/workspace/store/" + hostName + "-run" + key + ".txt"
    f = open(output, "w")
    #f.write(finalMultiplyOutput)
    f.writelines([finalMultiplyOutput,"\n",finalAdditionOutput])
    f.close()
    #print("{}".format(d))
#print(data["2"])


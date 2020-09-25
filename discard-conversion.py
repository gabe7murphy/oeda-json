import sys
import os
import json


def extract_name_and_comment(line):

    code_idx = line.index("#")

    name = line[0:code_idx].strip()
    code = line[code_idx:].strip()

    return name, code

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if len(sys.argv) < 2:
    print("Error: Provide Input Text File")
    sys.exit()

print ('Input File:' , str(sys.argv[1]))

inputactorfilename = sys.argv[1]

with open(inputactorfilename) as f:
     lines = f.readlines()

print (str(len(lines)))

#strip the end of testactor.txt
outputactorfilename = inputactorfilename.rsplit('.',1)[0] + '.json'

#with open(outputactorfilename, 'w') as f:  #write file and use meld to compare two files
#   f.writelines(lines) #check  

actorlist = []


actordict = {
    "name": "NONE",
    "comments": []
}    


for line in lines:

    line = line.strip()  #remove leading & trailing spaces

    if len(line) < 1 or line.startswith("#"):
        print("Skipping blank or comment")
        pass  

    else:   

        if "#" in line:
            code_idx = line.index("#")
            alias = line[0:code_idx].strip()
            comment = line[code_idx:].strip() 

            actordict["comments"].append(line)

            line = alias 

        else:   

            actor_name = ""
            codes = []

            actor_name = line
            

            if actordict["name"] != "NONE":
                actorlist.append(actordict)
                actordict = actordict = {
                "name": actor_name,
                "comments": []
                }    
            else:
                actordict["name"] = actor_name    
                actordict["codes"] = codes

actorlist.append(actordict)    

with open(outputactorfilename, 'w') as f:
    json.dump(actorlist, f, ensure_ascii=False, indent=4)


    

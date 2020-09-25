import sys
import os
import json


def extract_agent(line):

    agentdict = {
        "name": "",
        "name_plural": "",
        "code": "",
        "comment": ""
    }

    if "#" in line:
        tag = line.index("#")
        agentcomment = line[tag+1:].strip()
        agentdict["comment"] = agentcomment

    if "{" in line:
        openbrace = line.index("{")
        closebrace = line.index("}")
        plural = line[openbrace+1:closebrace].strip()
        agentdict["name_plural"] = plural
        agentname = line[:openbrace]
        agentdict["name"] = agentname


    if "[" and "]" in line:
        openbracket = line.index("[")
        closebracket = line.index("]")
        agentcode = line[openbracket+1:closebracket].strip()
        agentdict["code"] = agentcode
        agentname = line[:openbracket]
        agentdict["name"] = agentname
        
        
    if "[" and "]" and "{" in line:
        openbrace = line.index("{")
        agentname = line[:openbrace]
        agentdict["name"] = agentname


   
    

    return agentdict




def extract_substitutions(line):

    subdict = {
        "subcode": "",
        "subslist": []
    }


    equals = line.index("=")

    subcode = line[1:equals-2].strip()

    wordslist = line[equals+2:]
    subslist = wordslist.split(", ")

    subdict["subcode"] = subcode
    subdict["subslist"] = subslist

    return subdict



def main():

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

    outputdict = {
        "substitution_sets": [],
        "agents": []
    }

    for line in lines:

        line = line.strip()  #remove leading & trailing spaces

        if len(line) < 1 or line.startswith("#"):
            print("Skipping blank or comment")
            pass  

        else:   

            # check for substitution sets
            if "=" in line:
                substitution = extract_substitutions(line)
                outputdict["substitution_sets"].append(substitution)
                                        
            # check for name/plural/code/comment
            else:   
                if "[" in line:   
                    agent = extract_agent(line)
                    outputdict["agents"].append(agent)
                
    with open(outputactorfilename, 'w', encoding='utf-8') as f:
        json.dump(outputdict, f, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    main()
    print("DONE\n")

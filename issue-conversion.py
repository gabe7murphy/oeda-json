import sys
import os
import json


def start_issue(line):

    issuedict = {
        "category": "NONE",
        "type": "",
        "exclusion_phrases": [],
        "names":  []
        
    }  

    cat_idx = line.index("CATEGORY=") + 9
    type_idx = line.index("TYPE=") + 5
    end_idx = line.index(">")

    cat = line[cat_idx : type_idx-6].strip()
    itype = line[type_idx : end_idx].strip()

    issuedict["category"] = cat
    issuedict["type"] = itype

    return issuedict


def extract_name_and_code(line): 

    name_code_pair = {
        "name": "",
        "code": ""
    }

    code_idx = line.index("[")

    name = line[0:code_idx].strip()
    code = line[code_idx:].strip()

    name_code_pair["name"] = name
    name_code_pair["code"] = code

    return name_code_pair

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

    #with open(outputactorfilename, 'w') as f:  #write file and use meld to compare two files
    #   f.writelines(lines) #check  

    issues = []   # The list of issues
    issuedict = { }    # One issue

    for line in lines:

        line = line.strip()  #remove leading & trailing spaces

        if len(line) < 1 or line.startswith("#"):
            print("Skipping blank or comment")
            pass  

        if "</ISSUE>" in line:

            issues.append(issuedict)  # Previous issue is done, add to list
            #line = ""

        elif "<ISSUE" in line:  # start of a new issue
            issuedict = start_issue(line)

        else:   

            if "~" in line:
                code_idx = line.index("~")
                exclusion = line[code_idx:].strip() 

                issuedict["exclusion_phrases"].append(exclusion)
     
            else:
                if "[" in line:   
                    name_code_pair = extract_name_and_code(line)
                    issuedict["names"].append(name_code_pair)   

    with open(outputactorfilename, 'w') as f:
        json.dump(issues, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
    print("DONE\n")    

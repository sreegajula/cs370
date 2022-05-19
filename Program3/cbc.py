import json

def main():
    file1 = open('logins.json', 'r')
    lines = file1.readlines()

    count = 0

    for line in lines:
        
        person_dict = json.loads(line)

        if(person_dict["TimeCreated"] < "2021-03-16T12:00:09"):
            count += 1
            if("RemoteHost" in person_dict):
                if(person_dict["RemoteHost"] == "198.19.217.212"):
                    if("UserName" in person_dict):

 
    print(count)

    return 0

main()
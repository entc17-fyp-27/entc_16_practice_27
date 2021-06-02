import json
def GetInformation():
    print("You are requested to enter your valid information")
    name= input("Please enter your name ")
    age= input("Please enter your age ")
    city= input("Please enter your city ")
    telephone_number= input("Please enter your telephone number ")
    with open('UserInformations.json','r') as read_file:
        data = json.load(read_file)
    data[name]={"Age":age,"City":city,"Telephone Number":telephone_number}
    with open('UserInformations.json','w') as write_file:
        json.dump(data, write_file)
GetInformation()

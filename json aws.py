import json

with open('aws.json') as json_file:
    data = json.load(json_file)

count= data['count'] -1 #Get total count


for x in range(count):
    for y in range(20):
        try:
            print(data['results'][x]['configuration']['ipPermissions'][y]['toPort'])
        except:
            pass
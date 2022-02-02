"""
Export json file in aws config with security groups along with ports

"""

import json

with open('test.json') as json_file:
    data = json.load(json_file)

count= data['count'] -1 #Get total count

for x in range(count):
    print(data['results'][x]['accountId'])
    print(data['results'][x]['resourceId'])
    for y in range(25):
        try:
            print(data['results'][x]['configuration']['ipPermissions'][y]['toPort'])
        except:
            pass

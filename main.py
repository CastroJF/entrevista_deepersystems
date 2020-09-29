import json
data=None

with open('source_file_2.json') as f:
  data = json.load(f)

managers = []
for row in data:
    managers.append({'priority':row['priority'],'dados':row})

newlist = sorted(managers, key = lambda i: i['priority'],reverse=False) 

json_list = []
for row in newlist:
    json_list.append(row['dados'])

with open('managers.json', 'w') as json_file:
  json.dump(json_list, json_file)

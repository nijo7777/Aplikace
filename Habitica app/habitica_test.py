import requests as rq
import json

header = {"Content-type":"application/json","x-api-user":"8aa8744e-77e2-47e4-98c8-700d7ca6ad42","x-api-key":"12dfeed7-b90f-44a6-a1ca-859152c1cbc6","x-client":"8aa8744e-77e2-47e4-98c8-700d7ca6ad42-myAppForSVOB"}

url = "https://habitica.com/api/v3/tasks/user"

x = rq.get(url,headers=header)
# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(x.text)

habits = []
daily = []
todo = []

for f in response_dict['data']:
    if f['type'] == 'habit':
        habits.append(f['text'])
    elif f['type'] == 'daily':
        daily.append(f['text'])
    else:
        todo.append(f['text'])

print("Mám tyhle návyky:")
print(habits)
print("\nTyhle denní úkoly:")
print(daily)
print("\nA tyhle úkoly")
print(todo)

print("\nA chci je zobrazit ve třech sloupcích")
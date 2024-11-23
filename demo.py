import requests
import time

user_id1 = 922061821
sid1 = 'V02SdJIgPeHbKDhJVkgz7SPSuae7ODk00a4833ed0036f58bfd'
host = 'http://note-api.wps.cn'

url = host + '/v3/notesvr/set/notegroup'
headers = {
    'Cookie': f'wps_sid={sid1}',
    'X-user-key': str(user_id1),
    'Content-Type': 'application/json'
}

group_id = str(int(time.time() * 1000))
body = {
    "groupId": group_id,
    "groupName": 'test',
    "order": 0
}
res = requests.post(url, headers=headers, json=body)
assert res.status_code == 200
assert 'responseTime' in res.json().keys()
assert 'updateTime' in res.json().keys()
assert len(res.json().keys()) == 2
assert type(res.json()['responseTime']) == int
assert type(res.json()['updateTime']) == int

get_url = host + '/v3/notesvr/get/notegroup'
body = {'excludeInValid': True}
res = requests.post(get_url, headers=headers, json=body)
assert len(res.json()['noteGroups']) == 1
assert res.json()['noteGroups'][0]['groupId'] == group_id
assert res.json()['noteGroups'][0]['groupName'] == 'test'
assert res.json()['noteGroups'][0]['order'] == 0

url = host + '/v3/notesvr/set/notegroup'
headers = {
    'Cookie': f'wps_sid={sid1}',
    'X-user-key': str(user_id1),
    'Content-Type': 'application/json'
}

group_id = str(int(time.time() * 1000))
body = {
    "groupId": group_id,
    "groupName": 'test',
    "order": 0
}
body.pop('groupId')
res = requests.post(url, headers=headers, json=body)
print(res.status_code)
assert res.status_code == 400

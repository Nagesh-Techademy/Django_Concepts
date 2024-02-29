import requests
import json

URL="http://127.0.0.1:8000/api/studentapi/"

#To access the api's from OutSide
#GET ------------------------------------------------------------------------------------------------
def get_data(id = None): #step 2
    data = {}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    print(r)
    data= r.json()
    print(data)

#get_data(1)  #Step1
#print('For all')
get_data()

#POST-----------------------------------------------------------------------------------------------------
def post_data():
    data={
        'name':'raksha',
        'roll':120,
        'city':'Miraj'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    print(r)
    data = r.json()
    print(data)
# post_data()


def update_data():
    data={
        'id': 6,
        'name':'Omkar',  # if it is partial update then you can pass only required fileds
        'roll': 7,
        'city':'Sangli'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
#update_data()
#get_data() #To check Updated Data




def delete_data():
    data={
        'id': 4
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

#delete_data()


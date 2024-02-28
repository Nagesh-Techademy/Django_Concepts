import requests
import json

URL="http://127.0.0.1:8000/api/studentapi/"

#To access the api's from OutSide

def get_data(id = None): #step 2
    data = {}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    print(r)
    data= r.json()
    print(data)

# get_data(1)  #Step1
#print('For all')
get_data()

#
# #------------------------------------------------------------------------------
# import requests
#
# URL = "http://127.0.0.1:8000/api/studentapi/"
#
# def get_data(id=None):
#     params = {}
#     if id is not None:
#         params['id'] = id
#     r = requests.get(url=URL, params=params)
#     print(r)
#     if r.status_code == 200:
#         data = r.json()
#         print(data)
#     else:
#         print("Failed to fetch data. Status code:", r.status_code)
#
# get_data()


#POST-----------------------------------------------------------------------------------------------------
def post_data():
    data={
        'name':'Ravi',
        'roll':104,
        'city':'Dhanbad'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    print(r)
    data = r.json()
    print(data)
#post_data()


def update_data():
    data={
        'id': 5,
        'name':'Complete Update',  # if it is partial update then you can pass only required fileds
        'roll':107,
        'city':'Dharwad'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
update_data()
get_data() #To check Updated Data




def delete_data():
    data={
        'id': 5
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

delete_data()
print('After')
get_data() #To check Updated Data

import requests
import json
URL='http://127.0.0.1:8000/studentapi/'


# l want data get with id 1  and all data get // logic this method 
def get_data(id=None):
    datadis={}
    if id is not None:
        datadis={'id':id}
    json_data=json.dumps(datadis)
    r=requests.get(url=URL,data=json_data)
    
    data1=r.json()
    print(data1)
# get_data()
        
def post_data():
    insert={
        'name':"rmoshin",
        "roll":'100',
        'city':'jamalpur'        
    }
    insert1={
        'name':"Ajmal",
        "roll":'2005894',
        'city':'Qiampur'
        
    }
    json_data=json.dumps(insert)
    r=requests.post(url=URL,data =json_data)
    data=r.json()
    print(data)
post_data()

def update_data():
    insert={
        'id':8,
        'name':"mohsin",
        'city':'malsi'
        
    }
   
    json_data=json.dumps(insert)
    r=requests.put(url=URL,data =json_data)
    data=r.json()
    print(data)
# update_data()    
    
def delete_data():
    insert={'id':3}
   
    json_data=json.dumps(insert)
    r=requests.delete(url=URL,data =json_data)
    data=r.json()
    print(data)            
        
# delete_data()        
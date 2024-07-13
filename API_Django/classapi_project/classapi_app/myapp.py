import requests
import json
URL='http://127.0.0.1:8000/studentapi/'


# l want data get with id 1  and all data get // logic this method 
def get_data(id=None):
    datadis={}
    if id is not None:
        datadis={'id':id}
    json_data=json.dumps(datadis)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,data=json_data, headers=headers)
    
    data1=r.json()
    print(data1)
get_data()
        
def post_data():
    insert={
        'name':"shahzad",
        "roll":'115',
        'city':'mayachanu'
        
    }
    insert1={
        'name':"Ajmal",
        "roll":'2005894',
        'city':'Qiampur'
        
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(insert)
    r=requests.post(url=URL,data =json_data,headers=headers)
    data=r.json()
    print(data)
post_data()

def update_data():
    insert={
        'id':1,
        'name':"mohsin_allah wasaha",
        'city':'malsi',
        'roll':'5'
        
    }
   
    json_data=json.dumps(insert)
    headers={'content-Type':'application/json'}
    r=requests.put(url=URL,data =json_data, headers=headers)
    data=r.json()
    print(data)
update_data()    
    
def delete_data():
    insert={'id':1}
   
    json_data=json.dumps(insert)
    headers={'content-Type':'application/json'}
    r=requests.delete(url=URL,data =json_data,headers=headers)
    data=r.json()
    print(data)            
        
delete_data()        
import requests
from operator import itemgetter 

def request_data():
    res=requests.get("https://covid19-mohfw.herokuapp.com/states")
    
    if res.status_code!=200:
        raise Exception("ERROR:unsuccessful")
    data=res.json()
    data=data["states"]
    sorted_data=(sorted(data, key=itemgetter('total'),reverse=True))
    return sorted_data
    
    
def generate_tweet(data):
    s="Current  TOP states:\n"
    s+="\n"
    # Dict={ }
    # d={}
    # lis=[]
    #print("Current  TOP states:\n")
    
    for i in range(3):
        name=data[i]['state']
        total=data[i]['cases']
        active=data[i]['recoveries']
        cured=data[i]['deaths']
        death=data[i]['total']
        s+="Name : "+str(name)+"\n"
        s+="Cases : "+str(total)+"\n"
        s+="Recoveries : "+str(active)+"\n"
        s+="Deaths : "+str(cured)+"\n"
        s+="Total : "+str(death)+"\n"
        
        # print(f"Name : {name}")
        # print(f"Total : {total}")
        # print(f"Active : {active}")
        # print(f"Cured : {cured}")
        # print(f"Death : {death}")
        if(i<2):
            s=s+"---"+"\n"
            # print("-----------------")  #for character limit
    # print(s)
    return s

# dict_data=request_data()
# tweet=generate_tweet(dict_data)

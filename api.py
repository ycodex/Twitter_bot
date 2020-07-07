import requests
from operator import itemgetter 

def main():
    res=requests.get("http://covid19-india-adhikansh.herokuapp.com/states")
    
    if res.status_code!=200:
        raise Exception("ERROR:unsuccessful")
    data=res.json()
    data=data["state"]
    sorted_data=(sorted(data, key=itemgetter('active'),reverse=True))
    #return sorted_data
    s="Current  TOP states:\n"
    s+="\n"
    # Dict={ }
    # d={}
    # lis=[]
    #print("Current  TOP states:\n")
    
    for i in range(3):
        name=sorted_data[i]['name']
        total=sorted_data[i]['total']
        active=sorted_data[i]['active']
        cured=sorted_data[i]['cured']
        death=sorted_data[i]['death']
        s+="Name : "+str(name)+"\n"
        s+="Total : "+str(total)+"\n"
        s+="Active : "+str(active)+"\n"
        s+="Cured : "+str(cured)+"\n"
        s+="Death : "+str(death)+"\n"
        
        # print(f"Name : {name}")
        # print(f"Total : {total}")
        # print(f"Active : {active}")
        # print(f"Cured : {cured}")
        # print(f"Death : {death}")
        if(i<2):
            s=s+"-----------------"+"\n"
            # print("-----------------")  #for character limit
    
    return s


main()

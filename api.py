import requests
from operator import itemgetter 

def main():
    res=requests.get("https://covid19-mohfw.herokuapp.com/states")
    
    if res.status_code!=200:
        raise Exception("ERROR:unsuccessful")
    data=res.json()
    data=data["states"]
    sorted_data=(sorted(data, key=itemgetter('cases'),reverse=True))
    #return sorted_data
    s="Current  TOP states:\n"
    s+="\n"
    # Dict={ }
    # d={}
    # lis=[]
    #print("Current  TOP states:\n")
    
    for i in range(3):
        name=sorted_data[i]['state']
        total=sorted_data[i]['cases']
        active=sorted_data[i]['recoveries']
        cured=sorted_data[i]['deaths']
        death=sorted_data[i]['total']
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
            s=s+"-------"+"\n"
            # print("-----------------")  #for character limit
    # print(s)
    return s


main()

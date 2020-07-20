import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from operator import itemgetter 
import api 


# redundant function
# def req_and_sort():
    
#     r=requests.get("https://covid19-mohfw.herokuapp.com/states")
#     data=r.json()
#     data=data["states"]
#     sorted_data=(sorted(data, key=itemgetter('total'),reverse=True))
#     return sorted_data

def create_csv(sorted_data):    
    json_object = json.dumps(sorted_data, indent = 4) 
    with open("data.json", "w") as outfile: 
        outfile.write(json_object) 
            
    csv_data= pd.read_json("data.json")
    csv_data.to_csv("data.csv",index=None)

def extract_data():
    table = pd.read_csv("data.csv")
    table.head()

    name=[]
    total=[]
    cases=[]
    cured=[]
    death=[]
    f_data=[]

    for i in range(4):
            name.append(sorted_data[i]['state'])
            total.append(sorted_data[i]['total'])
            cases.append(sorted_data[i]['cases'])
            cured.append(sorted_data[i]['recoveries'])
            death.append(sorted_data[i]['deaths'])
            
    #test
    # print(total)
    # print(cases)
    # print(cured)
    # print(death)
    f_data.append(total)
    f_data.append(cases)
    f_data.append(cured)
    f_data.append(death)
    # print(f_data)
    return f_data


def plot_and_save_graph(f_data):
    X = np.arange(4)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(X + 0.00, f_data[0], color = 'b', width = 0.25, label="total")
    ax.bar(X + 0.20, f_data[1], color = 'y', width = 0.25, label="cases")
    ax.bar(X + 0.40, f_data[2], color = 'g', width = 0.25, label="cured")
    ax.bar(X + 0.60, f_data[3], color = 'r', width = 0.25, label="death")
    plt.legend()
    plt.xticks(np.arange(0,4), name )
    plt.title("Sorted based on total number of cases")
    plt.ylabel("cases")

    plt.savefig("post.png",bbox_inches='tight')


dict_data=api.request_data()
create_csv()
extracted_data=extract_data()
plot_and_save_graph(extracted_data)
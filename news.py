from bs4 import BeautifulSoup
import requests
import csv 


date=0
lis=[]
def req():
    URL = "https://www.mohfw.gov.in/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib') 
     
    table = soup.find('div', attrs = {'class':'row equal-height'}) 
    table2= table.find('div', attrs = {'class':'col-lg-4 col-md-4 col-sm-6 col-xs-12'}) 
    for s in table2.find("strong"):
        date=s
    return date,table2
    
    
                         

def read_and_compare(date):

    with open('db.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, skipinitialspace=True)
        lis=[]
        for row in spamreader:
            lis.append(row)
            if(date in row):
                return 0
            
        write(date,len(lis)-2)
        return 1 
        
        

   
def write(date,length):
    with open('db.csv','a') as csvfile:
        
        writer=csv.writer(csvfile)
        length+=2
        writer.writerow([length,date])
        
        
def post(table2):
    s=""
    s+='Latest updates from MOHFW\n'
    s+="-------------------------\n"
    s+=str(table2.find("a").contents[0])
    s+="\n"
    s+=table2.find("a")["href"]
    return s


# d,t=req()
# if(read_and_compare(d)):
#     tweets=post(t)
#     print(tweets)
        
        
        



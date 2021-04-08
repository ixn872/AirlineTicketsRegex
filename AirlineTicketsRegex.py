file_path="C:\Users\User\Desktop\str.txt"
LL=[]
with open(file_path, 'r') as current:
    if len(current.read(1)) == 0:
        print('FILE IS EMPTY')
    else:
        current.seek(0)
        for line in current:
            LL.append(line)
            print(line)


string = open(file_path, 'r').read()
#string=" ".join(string.split())
string = string.replace('\n',' ')
#print string
#result = re.findall(r"ETR(.*)\bPNR", string)
#x=[x.group() for x in re.finditer(r'ETR(.*)PNR',string)]
#result=re.findall(r"ETR|PNR",string)
#result
#while len(string)>=3:
    #if re.search(r"ETR",string):

string=string.split("ETR") 
size=len(string)
Reason=[]
i=0
while i<size:
    string[i]=string[i].split("PNR")
    Reason.append(string[i][0])
    i+=1

del Reason[0]  
Reason[-1]=re.sub(r"AUDIT.+"," ",Reason[-1])

for i in range(len(Reason)):
    
    Reason[i]=re.sub(r"([ ]{2})","",Reason[i])
    x=re.findall(r"\d\.\.",Reason[i])
    if re.search(r"\d\.\.",Reason[i]):
        Reason[i]=re.sub(r"\d\.\."," ",Reason[i])
    elif re.search(r"\N\b", Reason[i]):
        print "YOOOOO"
    print Reason[i],i



#Dictionary style, key will be ticket number. Based on ticket number will return desired result. Just need to insert the ticket numbers you want.
PNR=[]
Request_Date=[]
Comm_AMT=[]
TKT_AMT=[]
Ticket=[]

for line in LL:
    test=line
    pattern1=re.compile(r"\s{2,}(\d+)(\s+)(\S+)")
    try:
        found1 = re.search(pattern1, test).group(1)  
        Ticket.append(found1)
    except AttributeError:
        found1 = '' 
del Ticket[7]
for line in LL:
    test=line
    pattern1=re.compile(r"(\S+) (\S+)(-)(\s+)(\d.\d+)(\s+)(\S+) (\S+) (-) (\S+)(\s+)(\d+.\d+)")
    
    try:
        found1 = re.search(pattern1, test).group(5)  
        Comm_AMT.append(found1)
        found2 = re.search(pattern1, test).group(12)
        TKT_AMT.append(found2)
        #Request_Date.append(found2)

    except AttributeError:
        found1 = '' 


for line in LL:
    test=line
    pattern1=re.compile(r"PNR-(.+?)\b")
    
    try:
        found1 = re.search(pattern1, test).group(1)  
        PNR.append(found1)
        #Request_Date.append(found2)

    except AttributeError:
        found1 = ''
        
print len(PNR)

for line in LL:
    test=line
    pattern2=re.compile(r"REPORT-(.+?)\b")
    try:
        found2 = re.search(pattern2, test).group(1)  
        Request_Date.append(found2)

    except AttributeError:
        found1 = '' 

Surname=[]
Name=[]
for line in LL:
    test=line
    pattern3=re.compile(r"PNR-(.+?) \b(.+?)\b(.+?)\b(.+?)\b")
    try:
        found3 = re.search(pattern3, test).group(2)  
        Surname.append(found3)
        found3 = re.search(pattern3, test).group(4)  
        Name.append(found3)

    except AttributeError:
        found3 = ''


import itertools 
import pandas as pd
pd.set_option('display.max_columns', 100)  # or 1000
pd.set_option('display.max_rows', 100)  # or 1000
pd.set_option('display.max_colwidth', -1)  # or 199
L = list(itertools.repeat(Request_Date[0], len(PNR)))
print len(L),len(PNR),len(Ticket),len(TKT_AMT),len(Comm_AMT),len(Surname),len(Name),len(Reason)
DF=pd.DataFrame({"Request Data":L,"Airline Code":PNR,"Ticket Number":Ticket,"Ticket AMT":TKT_AMT,"Commision AMT":Comm_AMT,"Surname":Surname,"Name":Name,"Reason": Reason})
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')
print_full(DF)

#{"Request Data":L,"Airline Code":PNR,"Ticket Number":Ticket,"Ticket AMT":TKT_AMT,"Commision AMT":Comm_AMT,"Surname":Surname,"Name":Name,



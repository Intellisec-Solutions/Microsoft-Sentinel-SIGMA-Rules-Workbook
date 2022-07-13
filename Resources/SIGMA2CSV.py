import  yaml
import glob
import sys
import pandas as pd # pip3 install pandas


# Download them from https://github.com/SigmaHQ/sigma


print("[+] Getting MITRE ATT&CK Techniques from SIGMA Rules")

Local_Path = sys.argv[1]

Local_Queries = []
#Local_Path = "sigma-master/rules/"
SGM=[]

for rule in glob.iglob(Local_Path  + '**/**', recursive=True):
    if rule.endswith('.yml'): 
      #print(rule)
      with open(rule,'r',encoding='utf-8') as q: #errors='ignore'
        try:
          yaml_query = yaml.load(q, Loader=yaml.FullLoader)
          for j in range(len(yaml_query["tags"])):
            #print("[+] "+ (str(yaml_query["tags"][j]).replace("t","T")) +" "+str(rule))
            #print("[+] "+ (((str(yaml_query["tags"][j]).replace("t","T")).split("."))[1]).upper())
            SGM.append({"Techniques":(((str(yaml_query["tags"][j]).replace("t","T")).split("."))[1]).upper(),"Rule":str(rule)})
            
        except:
          pass

print("[+] Techniques were extracted from Local Queries Successfully")

df_rules = pd.DataFrame(SGM)
df_rules.to_csv("SIGMA.csv",index=False)
print("[+] The CSV file  SIGMA.csv was generated Successfully")

import json
import termcolor # pip3 install termcolor
import pandas as pd # pip3 install pandas
from pandas import read_excel 
import sys

print(termcolor.colored("[+] MITRE NAVIGATION LAYER 2 CSV CONVERTER","cyan"))
print("Usage: python3 MITRE2CSV.py <Navigation_Layer Path (.json)> <Output_CSV_File Path (.csv)> ")

Profile_PATH = sys.argv[1]
with open(Profile_PATH,"r") as r:
  Profile = json.load(r)


TechniqueIDs = []

# Get Technique IDs
print("[+] Getting MITRE ATT&CK Techniques from the Navigation Layer")
for i in range(len(Profile["techniques"])):
  #print(Profile["techniques"][i]["techniqueID"])
  TechniqueIDs.append({"TechniqueID":Profile["techniques"][i]["techniqueID"],"AtomicURL":Profile["techniques"][i]["comment"]})
  #print(Profile["techniques"][i]["tactic"])

# Get Technique Details

print("[+] Getting MITRE ATT&CK Details")
Techniques_file = "enterprise-attack-v11.2-techniques.xlsx"
sheet = "techniques"
Techniques_df = read_excel(Techniques_file, sheet_name = sheet)
data = Techniques_df[["ID","name","url","created","tactics","platforms"]].values.tolist()

#print(data[0])
#TechniqueIDs =  list(dict.fromkeys(TechniqueIDs)) # Remove Duplicates

print("[+] Generating the CSV file")
Technique_Details = []


for id in range(len(TechniqueIDs)):
    for technique in range(len(data)):
      if str(TechniqueIDs[id]["TechniqueID"]) == str(data[technique][0]):
        print(TechniqueIDs[id]["TechniqueID"])
        Technique_Details.append({"ID":data[technique][0],"name":data[technique][1],
          "url":data[technique][2],"created":data[technique][3],"tactics":data[technique][4],
                                "platforms":data[technique][5],"AtomicUrl":"https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/"+str(data[technique][0])+"/"+str(data[technique][0])+".md"})


Output = sys.argv[2]
df_Techniques = pd.DataFrame(Technique_Details)
df_Techniques.to_csv(Output,index=False)
print("[+] The CSV file ",Output," was generated Successfully")

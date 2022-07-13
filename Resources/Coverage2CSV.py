from pandas import read_excel  # pip3 install pandas
import pandas as pd


print("[+] Coverage to CSV")
Coverage_Techniques =[]
Coverage_excel_File = "Techniques.xlsx" # The excel file exported from Sentinel Workbook
sheet = "export_data.xlsx"
Techniques_Excel = read_excel(Coverage_excel_File, sheet_name = sheet)
Techniques = Techniques_Excel[["Techniques"]].values.tolist()
for v in Techniques:
  if str(v) != str("[nan]"):
    for i in v:
      Techs = list(i.split(","))
      Coverage_Techniques = Coverage_Techniques + Techs

Coverage_Techniques =  list(dict.fromkeys(Coverage_Techniques))
print(Coverage_Techniques)

df_Techniques = pd.DataFrame(Coverage_Techniques)
df_Techniques.to_csv("Coverage.csv",index=False, header=["ATTACKTechniques"])
print("[+] The CSV file  Coverage.csv  was generated Successfully")

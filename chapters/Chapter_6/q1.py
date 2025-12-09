1. Which Python module is used for reading and writing CSV files?
b) Dictionary for each row with column names as keys
c) Tuple for each row
import pandas as pd
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
import csv
with open("students.csv", mode="r") as file:
reader = csv.DictReader(file)
for row in reader:
if int(row["Grade"]) > 80:
print(row["Name"])
import json
data = {
with open("course.json", "w") as file:
json.dump(data, file, indent=4)
with open("course.json", "r") as file:
loaded_data = json.load(file)
print(loaded_data["students"])
import pandas as pd
data = {
df = pd.DataFrame(data)
df.to_excel("employees.xlsx", index=False)
loaded_df = pd.read_excel("employees.xlsx")
print(loaded_df[["Name", "Salary"]])
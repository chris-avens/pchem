from ucimlrepo import fetch_ucirepo
import seaborn as sns
import pandas as pd
  
# fetch dataset 
steel_industry_energy_consumption = fetch_ucirepo(id=851) 
  
# data (as pandas dataframes) 
X = steel_industry_energy_consumption.data.features 
y = steel_industry_energy_consumption.data.targets 
  
# metadata 
# print(steel_industry_energy_consumption.metadata) 
  
# variable information 
print(steel_industry_energy_consumption.variables) 

# head = sns.load_dataset('')

# for key in steel_industry_energy_consumption.metadata:
#     print(f"{key}: {steel_industry_energy_consumption.metadata[key]}")
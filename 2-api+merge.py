#%%
"""
Import packages needed
"""
# citation: https://docs.python.org/3/library/urllib.parse.html
# citation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.json_normalize.html
import requests
import pandas as pd
import os
from urllib.parse import urlencode
import matplotlib.pyplot as plt
import seaborn as sns 
#%%
os.chdir(r"C:\Users\Lucas Jiang\OneDrive - The University of Chicago\MPP\Fall 2022\DAP2-Python\Final Project")
wd = r"C:\Users\Lucas Jiang\OneDrive - The University of Chicago\MPP\Fall 2022\DAP2-Python\Final Project"
"""
Retrieve American Community Survey Data from American Census Bureau Website Through API
"""
class ACS_api():
    def __init__(self, year, interval, url, params, host = "https://api.census.gov/data"):
        self.host = host
        self.url = url
        self.year = year
        self.interval = interval
        self.params = params
        
    def _get(self,):
        url = self.host + "/" + str(self.year) + "/acs/acs" + str(self.interval) + "/" + str(self.url) +"?" + urlencode(self.params, safe = ':,')

        try:
            return requests.get(url).json()
        except:
            return requests.get(url).text
        
#%%
"""
Obtain the data and clean
"""
# for ACS data, the url is 'pums'
url = 'pums' 
year= 2019
# 1 for 1-year, 5 for 5-year
interval = 1
params = {
    # citation: https://api.census.gov/data/2004/acs/acs1/pums/variables.html for variable list
    # citation: https://www.census.gov/content/dam/Census/data/developers/api-user-guide/api-guide.pdf
    # citation: https://www.census.gov/data/developers.html
    "get": "SEX,AGEP,WAGP,SCHL",  
    "for": "state:*",
    "key": "37a7da353b7f14cacef8837f5ddf23800a8a33d6"
}

api = ACS_api(year=year, interval = interval,url = url, params = params)
response = api._get()

# convert to a data frame
acs_2019 = pd.DataFrame(response)
acs_2019 = acs_2019.rename(columns=acs_2019.iloc[0]).drop(acs_2019.index[0]).reset_index(drop=True)

# filter out peoplpe out of working ages
acs_2019 = acs_2019.apply(pd.to_numeric)
acs_2019 = acs_2019[acs_2019["AGEP"]>18]
acs_2019 = acs_2019[acs_2019["AGEP"]<65]

# Adding age group
# citation: https://stackoverflow.com/questions/52753613/grouping-categorizing-ages-column
age_bin = [18,20,25,30,35,40,45,50,55,60,65]
labels = ["18-20", "20-25", "25-30", "30-35", "35-40", "40-45", "45-50", "50-55", "55-60", "60-65"]
acs_2019["age_group"] = pd.cut(acs_2019["AGEP"], bins=age_bin, labels=labels, right=False)

# Filtering and dividing education attainment to High School & College or above
# citation: https://stackoverflow.com/questions/35666272/equivalent-of-r-ifelse-in-python-pandas-compare-string-columns
acs_2019 = acs_2019[acs_2019["SCHL"].isin([16, 20, 21, 22, 23, 24])]

def if_else(x, target, yes_label, no_label):
    if x == target:
        result = yes_label
    else:
        result = no_label
    return(result)

acs_2019["education_level"] = acs_2019["SCHL"].apply(lambda x: if_else(x, 16, "High School", "College or above"))
acs_2019["gender"] = acs_2019["SEX"].apply(lambda sex: if_else(sex, 1, "male", "female"))

#%%
"""
Import the state-fips conversion csv and merge with acs_2019
"""
state_fips = pd.read_csv(wd+r"\data\us-state-ansi-fips.csv")
state_fips.rename(columns={" st":"state", " stusps":"state_ab", "stname":"state_name"}, inplace=True)
acs_merge = acs_2019.merge(state_fips, on="state", how="left").dropna()
acs_merge["state_ab"] = acs_merge["state_ab"].str.strip()

#%%
"""
Output to a csv file for further usage
"""
acs_merge.to_csv(wd+r"\data\acs_merge.csv", index=False)
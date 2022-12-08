import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

wd = r"C:\Users\Lucas Jiang\OneDrive - The University of Chicago\MPP\Fall 2022\DAP2-Python\Final Project"

edu_df = pd.read_csv(wd+r"\data\mrc_table6.csv")

idx = edu_df['k_mean'].notnull()
edu_df = edu_df[idx]
edu_df = edu_df[['k_mean','tier']]
str_df = edu_df.groupby(["tier"]).mean(numeric_only=True)

fig, axs = plt.subplots(nrows=2)
sns.lineplot(data=str_df, 
             x="tier", 
             y = "k_mean",
             ax=axs[0])
sns.boxplot(data=edu_df, 
             x="tier", 
             y = "k_mean",
             ax=axs[1])

axs[0].set_title("School Tiers VS Kids Incomes")
axs[0].set_xlabel("")
fig.savefig(wd+r"\images\static1.png", bbox_inches="tight")


pk_df = pd.read_csv(wd+r"\data\mrc_table1.csv")
pk_df = pk_df[pk_df["state"]=="LA"]

np_parents = np.array(pk_df["par_median"])
np_kids = np.array(pk_df["k_median"])


plt.figure(figsize=(8, 6))
plt.scatter(np_parents, np_kids, s=20)

plt.title('Kids Incomes VS Parents Incomes')
plt.xlabel('Parents Incomes', labelpad=15)
plt.ylabel('Kids Incomes', labelpad=15)

fg = np.polyfit(np_parents.flatten(), np_kids.flatten(), 1)
c,d = fg[0],fg[1]
x = np.linspace(min(np_parents), max(np_parents),100)
plt.plot(x, c * x + d, 'k-')
plt.savefig(wd+r'\images\static2 and model fitting.png')

"""
We can see there is a significant positive relationship between kids'income and parents'income, and the correlation is 0.188148
hence the model can be: ParentIncome = 22704.23965 + 0.188148*KidsIncome + e
"""
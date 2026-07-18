import pandas as pd
from IPython.display import display
import numpy as np


df = pd.read_csv("logs.csv")

groups = np.array_split(df, 6)


fails = df[df["event"] =="FAIL"]

all_fails = []

for group in groups:
    fails = group[group["event"] == "FAIL"]
    fail_counts = fails.groupby("user").size().reset_index(name="fail_count")
    fail_counts = fail_counts.sort_values("fail_count", ascending=False).reset_index(drop = True)
    all_fails.append(fail_counts)





for i in range(len(groups)):

    all_fails[i]["risk_level"] = np.where(
    all_fails[i]["fail_count"] >= 3,
    "Suspicious",
    "Clear")



d = pd.concat(all_fails)



users_with_fail = d.loc[d["risk_level"] == "Suspicious", "user"]

dfinal = d[(d["risk_level"] == "Suspicious") | (~d["user"].isin(users_with_fail))]


dfinal["reason"] = np.where(dfinal["risk_level"] == "Suspicious","3+ failures within one log window","Threshold not reached")


print("FAILED LOGIN COUNTS:")

display(dfinal)


    
    


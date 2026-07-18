import pandas as pd
import random
from datetime import datetime, timedelta

df = pd.DataFrame()

names = [
    'Alex', 'Carol', 'Jeff', 'Bobby', 'Jesse', 
    'Camron', 'Julian', 'Hannah', 'Emily', 'Mathew',
    'Sarah', 'Daniel', 'Olivia', 'Nathan', 'Sophia',
    'Ethan', 'Mia', 'Lucas', 'Ava', 'Noah'
]

outcome_pool = ['FAIL', 'SUCCESS']
event_time = datetime(2026, 9, 1, 10, 0, 0)

ips = [
    "192.168.1.1",
    "192.168.1.2",
    "10.0.0.1",
    "10.0.0.2",
    "45.33.12.8",
    "185.220.101.45",
    "172.16.5.23",
    "203.0.113.77",
    "198.51.100.42",
    "8.8.4.4",
    "192.168.2.15",
    "10.1.0.25",
    "172.20.10.5",
    "104.26.3.12",
    "23.45.67.89",
    "66.249.66.1",
    "151.101.1.69",
    "34.117.59.81",
    "52.85.132.44",
    "13.107.42.14"
]

time_list = []
ip_list = []
names_list = []
outcome_list = []



while len(names) > 0 :
    i = random.choice(range(len(names)))
    event_time += timedelta(seconds=1)
    time_list.append(event_time)
    ip_list.append(ips[i])
    names_list.append(names[i])



    if names[i] in ['Camron', 'Julian']:
        outcome = random.choices(outcome_pool, weights=[95, 5], k=1)[0]
    else:
        outcome = random.choices(outcome_pool, weights=[40, 60], k=1)[0]

    outcome_list.append(outcome)

    if outcome == "SUCCESS":
        names.remove(names[i])
        ips.remove(ips[i])
       
  
       
  


df["timestamps"] = time_list
df["IP"] = ip_list
df["user"] = names_list
df["event"] = outcome_list

df.to_csv("logs.csv", index=False)
print(df)

import sqlite3
import pandas as pd
import numpy as np


conn = sqlite3.connect("security.db")



query = """SELECT datetime((strftime('%s', timestamps) / 10) * 10, 'unixepoch') AS time_window,
user,COUNT(*) AS fail_count
FROM logs
WHERE event = 'FAIL'
GROUP BY time_window, user;"""


df = pd.read_sql(query, conn)


df["risk_level"] = np.where(df["fail_count"] >= 3,"Suspicious", "Clear")


df["reason"] = np.where(df["risk_level"] == "Suspicious","3+ failures within one log window","Threshold not reached")


alerts = df[df["risk_level"] == "Suspicious"]


summary = (alerts.groupby("user").agg(suspicious_windows=("user", "count"),max_failures=("fail_count", "max") )
.reset_index().sort_values("max_failures", ascending=False))



df.to_csv("full_security_report.csv", index=False)

alerts.to_csv("security_alerts.csv", index=False)

summary.to_csv("security_summary.csv", index=False)


# Print results
print("SECURITY ANALYTICS REPORT")
print("-------------------------")

print("\nSuspicious Activity:")
print(alerts)

print("\nUser Risk Summary:")
print(summary)


conn.close()






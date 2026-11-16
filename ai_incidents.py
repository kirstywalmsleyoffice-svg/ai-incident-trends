import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/UserPC/Downloads/backup-20261102100724 (1)/mongodump_full_snapshot/incidents.csv")
print("Total incidents:", len(df))

df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year

per_year = df["year"].value_counts().sort_index()
print(per_year)
recent = per_year[per_year.index >= 2010]


plt.bar(recent.index, recent.values)
plt.title("Reported AI incidents by year (2026 provisional, to 2 November)") 
plt.ylabel("Number of incidents")
plt.xticks(recent.index, rotation=45)
plt.tight_layout()
plt.show()
input("Press Enter to close")
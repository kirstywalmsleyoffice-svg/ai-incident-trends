import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/UserPC/Downloads/backup-20261102100724 (1)/mongodump_full_snapshot/incidents.csv")
print("Total incidents:", len(df))

df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
dep ="Alleged deployer of AI system"
df["misuse"] = df[dep].str.contains("scammers|deepfake-creators|synthetic-media-creators|information-manipulation-actors|cybercriminals")
print("Misuse incidents:",df["misuse"].sum())
per_year = df["year"].value_counts().sort_index()
misuse_per_year = df[df["misuse"]]["year"].value_counts().sort_index()
print(misuse_per_year)
share = (misuse_per_year / per_year * 100).round()
print(share[share.index >= 2017])

recent = share[share.index >= 2017]
plt.bar(recent.index, recent.values)
plt.title("Share of reported AI incidents involving misuse (2026 provisional)") 
plt.ylabel("Share of reported incidents (%)")
plt.xticks(recent.index, rotation=45)
plt.tight_layout()
plt.savefig("C:/Users/UserPC/Downloads/misuse_share.png", dpi=150)
plt.show()

input("Press Enter to close")
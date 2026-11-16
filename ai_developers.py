import pandas as pd

df = pd.read_csv("C:/Users/UserPC/Downloads/backup-20261102100724 (1)/mongodump_full_snapshot/incidents.csv")

dev= "Alleged developer of AI system"
dep= "Alleged deployer of AI system"

devs = df[dev].str.strip("[]").str.replace('"',"").str.split(",").explode()
deps = df[dep].str.strip("[]").str.replace('"',"").str.split(",").explode()
print(deps.value_counts().head(15))

for name in ["openai", "google","tesla","anthropic"]:
	print(name,"developer:",(devs== name).sum(),"deployer:",(deps == name).sum())
input("Press Enter to close")
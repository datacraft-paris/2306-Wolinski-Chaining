# RemoteWork

pd.crosstab(df.MainBranch, df.RemoteWork)

remote_cat = pd.CategoricalDtype(["Remote", "Hybrid", "Office"], ordered=True)

var = df.RemoteWork.map({"Fully remote": "Remote",
                         "Hybrid (some remote, some in-person)": "Hybrid",
                         "Full in-person":"Office"}).astype(remote_cat)

pd.crosstab(df.MainBranch, var)

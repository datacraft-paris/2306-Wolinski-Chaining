# Technos

cols = [col for col in df.columns if col.endswith("HaveWorkedWith")]
haveworkedwith = df[cols].apply(lambda row: ';'.join(row.dropna().astype(str)), axis=1).str.get_dummies(";").sum()

cols = [col for col in df.columns if col.endswith("WantToWorkWith")]
wantoworkwith = df[cols].apply(lambda row: ';'.join(row.dropna().astype(str)), axis=1).str.get_dummies(";").sum()

fig, ax = plt.subplots(figsize=(8, 8))
(wantoworkwith/haveworkedwith).nlargest(30).plot.barh(ax=ax, title="Ratio d'intérêt des langages");

(wantoworkwith/haveworkedwith).loc[["Java", "C++", "Python", "Go", "Julia", "Rust"]].plot.barh(title="Ratio d'intérêt des langages");

(wantoworkwith/haveworkedwith).loc[[lang for lang in wantoworkwith.index if lang.find("js")!=-1]].sort_values().plot.barh(title="Ratio d'intérêt des langages");

# OrgSize

var = df.OrgSize.replace("Just me - I am a freelancer, sole proprietor, etc.", "1")
var = var.str.replace(",", "").str.extract("^(\d+)", expand=False).fillna(0).astype(int)
thresholds = sorted(var.unique())
thresholds = thresholds[1:]
thresholds.append(np.inf)
var = pd.cut(var, thresholds, right=False)
var.value_counts(dropna=False, sort=False)

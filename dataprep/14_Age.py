# Age

var = df.Age.replace("Under 18 years old", "15")
var = var.str.extract("^(\d+)", expand=False).fillna(0).astype(int)
thresholds = sorted(var.unique())
thresholds = thresholds[1:]
thresholds.append(np.inf)
var = pd.cut(var, thresholds, right=False)
var.value_counts(dropna=False, sort=False)

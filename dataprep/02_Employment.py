# Employment

df.Employment.nunique()

df.Employment.value_counts().head(20)

df.Employment.value_counts(normalize=True).head(20).cumsum()

df.Employment.str.get_dummies(";")

df.Employment.str.get_dummies(";").columns

var = df.Employment.fillna("").apply(lambda x : x.startswith(("Employed", "Independent")))
var.value_counts()

# Gender

df.Gender.nunique()

df.Gender.value_counts().head(20)

df.Gender.value_counts(normalize=True).head(20).cumsum()

df.Gender.str.get_dummies(";")

df.Gender.str.get_dummies(";").columns

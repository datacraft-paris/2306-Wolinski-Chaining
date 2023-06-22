# SOPartFreq

df.SOPartFreq.unique()

sopartfreq_cat = pd.CategoricalDtype(['I have never participated in Q&A on Stack Overflow', 'Less than once per month or monthly', 'A few times per month or weekly', 'A few times per week', 'Daily or almost daily', 'Multiple times per day'], ordered=True)
var = df.SOPartFreq.astype(sovisitfreq_cat)

var.value_counts(dropna=False).sort_index()

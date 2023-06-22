# SOVisitFreq

df.SOVisitFreq.unique()

sovisitfreq_cat = pd.CategoricalDtype(['Less than once per month or monthly', 'A few times per month or weekly', 'A few times per week', 'Daily or almost daily', 'Multiple times per day'], ordered=True)
var = df.SOVisitFreq.astype(sovisitfreq_cat)

var.value_counts(dropna=False).sort_index()

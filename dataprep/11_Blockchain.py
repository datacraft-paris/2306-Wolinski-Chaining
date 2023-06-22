# Blockchain

df.Blockchain.unique()

blockchain_cat = pd.CategoricalDtype(['Very unfavorable', 'Unfavorable', 'Indifferent', 'Favorable', 'Very favorable'], ordered=True)
var = df.Blockchain.astype(blockchain_cat)

var.value_counts(dropna=False).sort_index()

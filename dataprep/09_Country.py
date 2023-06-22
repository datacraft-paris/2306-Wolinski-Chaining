# Country

var = pd.read_html("https://www.geonames.org/countries/", encoding="latin1")
[d.shape for d in var]
countries = var[1]

iso_country = countries.set_index("Country")["ISO-3166 alpha3"]
df["Country"].map(iso_country).value_counts()

set(df["Country"].unique()).difference(set(countries["Country"].values))

var = df["Country"].apply(lambda x: mapping_country.get(x, x)).map(iso_country)
var.value_counts(dropna=False).head(30)

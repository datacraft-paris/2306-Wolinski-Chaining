# EdLevel
df.EdLevel.unique()

def clean_edlevel(string):
    match string.split()[0]:
        case "Associate":
            return "Undergraduate"
        case "Bachelor’s":
            return "Undergraduate"
        case "Master’s":
            return "Master"
        case "Other":
            return 'PhD'
        case "Primary/elementary":
            return "NoHigherEd"
        case "Secondary":
            return "NoHigherEd"
        case "Professional":
            return "Misc"
        case _:
            return np.nan

var = df.EdLevel.fillna("none").apply(clean_edlevel)
var.value_counts()

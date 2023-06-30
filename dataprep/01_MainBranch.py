# MainBranch

df.MainBranch.value_counts()

var = df.MainBranch.apply(lambda x: 'Dev' if x == 'I am a developer by profession' else 'NotDev')

var = df.MainBranch.where(df.MainBranch == 'I am a developer by profession', 'NotDev')

var = df.MainBranch.mask(df.MainBranch == 'I am a developer by profession', 'Dev')

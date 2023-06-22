# LearnCode, LearnCodeOnline, LearnCodeCoursesCert

learn_code_cols = [col for col in df.columns if col.startswith("LearnCode")]

for col in learn_code_cols:
    print(col, df[col].str.get_dummies(";").columns)

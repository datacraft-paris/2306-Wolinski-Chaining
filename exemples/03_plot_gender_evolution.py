# gender evolution graph for a name
def plot_gender_evolution(df, name):
    """Plot the gender evolution of a given name"""
    return (df
            .loc[lambda df_: df_.name==name]
            .pivot_table(values='births',
                         index='year',
                         columns='gender',
                         fill_value=0)
            .pipe(lambda df_: df_.div(df_.sum(axis=1), axis=0))
            .plot
            .line(title=f'Evolution du genre de {name} au fil des ans', color=['m', 'c'])
            .legend(bbox_to_anchor=(1.2, 1.0))
    )

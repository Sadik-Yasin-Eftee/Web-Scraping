import pandas as pd


def reviewFilter(df, keyphrases):
    filtered_df = df[df['Review Content'].str.contains('|'.join(keyphrases), case=False, na=False)]
    return filtered_df
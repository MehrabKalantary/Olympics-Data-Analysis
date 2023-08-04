import pandas as pd


def preprocess(df, region_df):
    """
    Cleaning and preparing two datasets
    1. Filtering
    2. Merging
    3. Dropping duplicates
    4. One hot encoding medals
    :param df: Athlete dataset
    :param region_df: NOC regions dataset
    :return Cleaned dataset:
    """
    df = df[df['Season'] == 'Summer']
    df = df.merge(region_df, on='NOC', how='left')
    df.drop_duplicates(inplace=True)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df

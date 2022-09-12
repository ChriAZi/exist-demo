import pandas as pd

from clean_data import clean_data


def load_dataframe():
    return pd.read_csv('data/train.csv')


def get_df_cleaned(extra_cols=False):
    df_train = load_dataframe()
    df_cleaned = clean_data(df_train, False)
    df_cleaned['SurvivedText'] = df_cleaned['Survived']
    df_cleaned['SurvivedText'].loc[df_cleaned['SurvivedText'] == 0] = 'Died'
    df_cleaned['SurvivedText'].loc[df_cleaned['SurvivedText'] == 1] = 'Survived'
    if not extra_cols:
        df_cleaned = df_cleaned.drop(['PassengerId', 'Age', 'Sex', 'SurvivedText'], axis=1)
    return df_cleaned

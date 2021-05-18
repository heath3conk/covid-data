import pandas as pd
from datetime import timedelta

nytimes_data_url = 'https://github.com/nytimes/covid-19-data/raw/master/us-counties.csv'


def fetch_times_data():
    return pd.read_csv(nytimes_data_url)


def make_common_key(row):
    return str(row['fips']) + str(row['date'])


def add_common_index(df):
    modified_df = df.copy()
    modified_df['fips_date_index'] = modified_df.apply(make_common_key, axis=1)
    return modified_df


def yesterdays_date(row):
    current_date = pd.to_datetime(row['todays date'])
    yesterday = current_date - timedelta(days=1)
    return yesterday.strftime('%Y-%m-%d')


def adapt_yesterdays_data(df):
    df = df.rename({'date': 'todays date'}, axis=1)
    df['date'] = df.apply(yesterdays_date, axis=1)
    df = df.rename({'cases': 'cumulative cases'}, axis=1)
    df = df.rename({'deaths': 'cumulative deaths'}, axis=1)
    return df


def finalize_columns(df):
    df['daily cases'] = df['cumulative cases'] - df['cases']
    df['daily deaths'] = df['cumulative deaths'] - df['deaths']
    columns_to_keep = ['todays date', 'county', 'state', 'fips', 'cumulative cases', 'cumulative deaths', 'daily cases',
                       'daily deaths']
    return df.filter(columns_to_keep, axis=1)


def get_ny_times_data():
    original_data_df = fetch_times_data()
    previous_days_df = adapt_yesterdays_data(original_data_df)
    previous_with_index_df = add_common_index(previous_days_df)
    original_with_index_df = add_common_index(original_data_df)
    joined_df = original_with_index_df.merge(previous_with_index_df, how='left')
    return finalize_columns(joined_df)

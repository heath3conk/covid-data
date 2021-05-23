import random


def get_random_sample(df):
    start_location = random.randrange(700000, 1300000)
    end_location = start_location + 100
    sample_df = df.iloc[start_location:end_location]
    sample_df.to_csv('random-sample.csv')


def check_nan_value_fips(df):
    nan_df = df[df['fips'].isna()]
    nan_df.to_csv('nan-fips.csv')
    ri_df = df.loc[df['state'] == 'Rhode Island']
    ri_df.to_csv('all-rhode-island.csv')


def manually_check_math(df):
    last_entry_fips = df.iloc[-1]['fips']
    df_last_entry_county = df.loc[df['fips'] == last_entry_fips]
    df_last_entry_county.to_csv('county.csv')


def run_sanity_checks(df, args):
    get_random_sample(df)
    if 'details' in args:
        check_nan_value_fips(df)
        manually_check_math(df)
    print('Sanity checks finished.')

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


def check_edges(df):
    print('Result contains ' + str(len(df)) + ' rows.')
    print('The date in the last row of the results is ' + str(df.iloc[-1]['date']))
    data_first_date = '2020-01-21'
    eval_first_row = str(df.iloc[0]['date']) == data_first_date
    print('First row has correct date: ' + str(eval_first_row))
    print('First row:')
    print(df.iloc[0])
    print('*******************')
    print('Last row:')
    print(df.iloc[-1])


def manually_check_math(df):
    last_entry_fips = df.iloc[-1]['fips']
    df_last_entry_county = df.loc[df['fips'] == last_entry_fips]
    df_last_entry_county.to_csv('county.csv')


def run_sanity_checks(df, args):
    check_edges(df)
    get_random_sample(df)
    if 'details' in args:
        check_nan_value_fips(df)
        manually_check_math(df)

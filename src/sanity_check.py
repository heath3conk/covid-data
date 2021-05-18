import random
import datetime


def get_random_sample(df):
    start_location = random.randrange(1000000, 3000000)
    sample_df = df.iloc[start_location:start_location+30]
    sample_df.to_csv('random-sample.csv')


def check_nan_value_fips(df):
    df = df[df['fips'].isna()]
    df.to_csv('nan-fips.csv')


def check_edges(df):
    data_first_date = '2020-01-22'
    eval_first_row = str(df.iloc[0]['todays date']) == data_first_date
    print('First row has correct date: ' + str(eval_first_row))
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    eval_last_row = str(df.iloc[-1]['todays date'])
    print(df.iloc[-1])


def run_sanity_checks(df):
    check_edges(df)
    get_random_sample(df)
    check_nan_value_fips(df)

import pandas as pd
from time import time
from sanity_check import run_sanity_checks


def get_nytimes_data():
    nytimes_data_url = 'https://github.com/nytimes/covid-19-data/raw/master/us-counties.csv'
    df = pd.read_csv(nytimes_data_url)
    df['daily cases'] = df.groupby('fips')['cases'].diff()
    df['daily deaths'] = df.groupby('fips')['deaths'].diff()
    return df


def get_population_data():
    population_url = 'https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv'
    df = pd.read_csv(population_url, encoding='latin_1')
    df['COUNTY'] = df['COUNTY'].astype(str)
    df['COUNTY'] = df.COUNTY.str.pad(3, side='left', fillchar='0')
    df['STATE'] = df['STATE'].astype(str)
    df['fips'] = df['STATE'] + df['COUNTY']
    df['fips'] = df['fips'].astype(int)
    final_columns = {'POPESTIMATE2019', 'fips'}
    return df.drop((set(df.columns) - final_columns), axis=1)


def run_faster_version(args):
    start = time()
    ny_times_df = get_nytimes_data()
    population_df = get_population_data()
    result = ny_times_df.merge(population_df, on='fips', how='left')
    result.to_csv('covid_data.csv')
    print('Processing time = ' + str(time() - start) + ' seconds.')
    if 'sanity' in args:
        print('Now starting sanity checks.')
        run_sanity_checks(result, args)

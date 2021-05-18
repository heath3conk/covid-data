import pandas as pd

population_url = 'https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv'


def make_fips(row):
    county = row['COUNTY']
    if county != 0:
        if county < 10:
            fips = str(row['STATE']) + '00' + str(county)
            return int(fips)
        if county < 100:
            fips = str(row['STATE']) + '0' + str(county)
            return int(fips)
        else:
            fips = str(row['STATE']) + str(county)
            return int(fips)
    else:
        return 0


def add_fips_column(df):
    df['FIPS'] = df.apply(make_fips, axis=1)
    return df


def dictify(df):
    real_counties = df.loc[df['FIPS'] != 0]
    real_counties = real_counties.set_index('FIPS')
    real_counties = real_counties.filter(['POPESTIMATE2019'])
    return pd.Series(real_counties.POPESTIMATE2019.values, index=real_counties.index).to_dict()


def get_population_data():
    population_df = pd.read_csv(population_url, encoding='latin_1')
    smaller_pop_df = population_df.filter(['STATE', 'COUNTY', 'POPESTIMATE2019'], axis=1)
    smaller_pop_df = add_fips_column(smaller_pop_df)
    return dictify(smaller_pop_df)

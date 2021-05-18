from population import get_population_data


population_dict = get_population_data()


def get_population(row):
    fips = row['fips']
    result = population_dict.get(fips)
    if result:
        return result
    else:
        return 0


def add_population_data(df):
    df['population'] = df.apply(get_population, axis=1)
    return df

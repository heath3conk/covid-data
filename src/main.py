import sys
from nytimes import get_ny_times_data
from merge_data import add_population_data
from sanity_check import run_sanity_checks


def run():
    args = sys.argv
    covid_df = get_ny_times_data(args)
    complete_df = add_population_data(covid_df)
    complete_df.to_csv('covid-data.csv')
    if 'sanity' in args:
        run_sanity_checks(complete_df, args)


if __name__ == '__main__':
    run()

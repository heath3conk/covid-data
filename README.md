# Code Exercise: Covid Data

## Running the script
1. In a terminal window, navigate to the src directory
2. Execute `python3 main.py`
3. Wait ~~a few minutes~~ about 18 seconds.
4. Look for the output 'covid_data.csv' in the src directory.

### Running the script with the 'sanity' option
If you want to see some results but don't want to open a csv file with over 1.3 million rows, follow the 
process above and add the 'sanity' argument at the end, so the execute command is `python3 main.py sanity`.

In addition to the complete csv file, this option generates four other csv files:
 - 100-row 'random-sample.csv' file from somewhere in the middle of the data if you just want to see, you know, a random sample.
 - The entire dataset for a random county in the 'county.csv'.
 - The entire dataset for Rhode Island in the 'all-rhode-island.csv'.
 - The 'nan-fips.csv' with all the rows that have empty 'fips' values and therefore no population figures.

Run the script as `python3 main.py sanity details` and you'll get the entire dataset for a single county in the 'county.csv'
as well as 'nan-fips.csv' file that collects those rows without 'fips' values. 


## What I would improve
1. Adding population for some of the entries without fips values - these seem to fall into two different categories
   - *Entities that are not counties:* 
      - Several cities, including New York City, Kansas City and Joplin, Missouri are included in the NYTimes data. 
        Kansas City and Joplin each exist in more than one county, so their cases and deaths are divided in multiple other 
        rows for a given day. New York City is in just one county but...it is the NYTimes so I guess it's understandable
        that they would include a separate line item for their home city. None of these cities has a 'fips' value in the data
        but, if we wanted to include their population, we could probably get it from somewhere and build that into the process.
      - The NYTimes data also includes data from Puerto Rico, Guam, the Northern Mariana Islands, Virgin Islands, etc. 
        Similar to the NYC data, we could probably get population data for these regions and build that in.
   - *Data from states where 'county' = 'Unknown':* I believe these rows represent state-wide data. I'd want to confirm 
     this assumption is correct and match these rows with the state-wide population data.
2. Adding tests.
   - *Tests > running with optional 'sanity' arg* 
   - Some of the tasks I've handled in the sanity_check module could be tests instead.
3. Error handling.
    - Connection errors in trying to fetch the original csv files. 
    - Decoding errors generated while converting the original csv files to dataframes.
     
## Sanity checks
As I thought of ways to check that my results were making sense, I generally added them to my 'sanity_check' module.
 - Looking at the single county's csv and the random-sample csv helps me understand the data in a sort of wide and deep way.
   The random sample gives me the wide view, where I can verify that the columns and generally the data in the columns show
   up as expected. The single county's data gives me the deep view to see how the data changes over time and validate that the
   math I'm doing to calculate the daily cases and daily deaths makes sense. It also helped me understand the occasional negative
   number for daily cases or daily deaths that I had seen in the random sample data.

As I was figuring out how to approach the problem, I ran several other checks that are now represented in the code:
- Validating how to manufacture a 'fips' code from the census data by looking at the first few rows of the NYTimes data
and finding those counties in the census data.
- I continue to be glad I grew up in Rhode Island because it comes to mind easily as a mini data set to review. This is how 
  I figured out that the census data includes a county code of '0' to show the state's entire population. 
  (As a point of interest, RI has only five counties.)
  
## Versions and Portability
- I ran this using Python 3.7 and Pandas 1.2.4.
- I successfully ran the script on both a Mac and Windows 10. Just checking.
    
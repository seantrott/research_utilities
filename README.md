Utility methods for concatenating files and scraping information from dataframes.

This is aimed at data files that are generated from jsPsych.

# Examples

## Merge subject files from a directory

If you have .csv files for each subject stored in a directory, you can read them in and create a merged pandas DataFrame:

```
from research_utilities.reformatting import concat_files

merged = concat_files({path_to_directory})
```

## Extract demographic information for each subject

If you have demographic-related questions at the end of your survey, often it is desirable to extract those answers and put them into an entirely new column (as opposed to the default `responses` column for jsPsych). 

The `scrape_demographic_info` function should be useful for this:

```
from research_utilities.reformatting import scrape_demographic_info

scraped_df = scrape_demographic_info(merged, filter_name="demographic1", 
									 new_col_name="Gender", question_label="Q0")
```

More details are given in the documentation, but the idea is that you can parameterize the process by which question/answer pairs you want to retrieve, then assign a *label* to the response that is retrieved (e.g. "Age", "Gender", etc.). This information is extracted by-subject, then merged with the original dataframe that was passed in, so these variables can be used as random or fixed effects in an analysis.
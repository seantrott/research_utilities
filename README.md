Utility methods for concatenating files, dataframes, etc.

# Merge subject files from a directory

If you have .csv files for each subject stored in a directory, you can read them in and create a merged pandas DataFrame:

```
from research_utilities.reformatting import concat_files

concat_files({path_to_directory})
```


"""Utilities for reformatting and reorganizing data."""

import os.path as op
import pandas as pd 
import json

from os import listdir


def concat_files(path_to_files):
    """Read in all .csv files in directory, concat to single dataframe.

    Parameters
    ----------
    path_to_files: str
      path to directory containing subject .csv files

    Returns
    -------
    pandas.DataFrame
      dataframe containing concatenated .csv files
    """
    files = listdir(path_to_files)
    frames = []
    for filename in files:
        if filename.split(".")[-1] == "csv":
            frames.append(pd.read_csv(op.join(path_to_files, filename)))
    return pd.concat(frames)


def scrape_demographic_info(dataframe, filter_name="demographic1", subject_col_name="subject", 
                            marker_col_name="type", response_col_name="responses",
                            question_label="Q0", new_col_name="Gender"):
    """Grab info from relevant column, then propagate to all rows.

    Use-case: 
    scrape_demographic_info(dataframe, filter_name="demographic1", question_label="Q0", new_col_name="Gender")
    Produces df with new column labeled "Gender", filled with answers to Q0. 

    Note that this assumes subject responses for a page are stored in JSON-like struct,
    e.g. {'Q0': 'Male', 'Q1': 22}

    Parameters
    ----------
    dataframe: pandas.DataFrame
      dataframe with subject responses
    filter_name: str
      name of relevant stimulus type to filter on, e.g. 'demographic1'
    subject_col_name: str
      name of column containing subject ids
    marker_col_name: str
      name of column that specifies stimulus type, e.g. one of {'stimType', 'type', etc.}
    response_col_name: str
      name of column with subject responses
    question_label: str
      name of question to grab info about, e.g. 'Q0' or 'Q1'
    new_col_name: str
      name of new column to create

    Returns
    -------
    pandas.DataFrame
      input dataframe merged with new information (e.g. gender or age)
    """
    filtered = dataframe[dataframe[marker_col_name]==filter_name]
    answers = [json.loads(response)[question_label] for response in list(filtered[response_col_name])]
    subj_demo = pd.DataFrame({'subject': filtered[subject_col_name],
                              new_col_name: answers})
    return pd.merge(dataframe, subj_demo)
    
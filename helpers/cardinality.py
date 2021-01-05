import pandas as pd
import numpy as np
# ---------------------------------------------------------------------------------------

from os import path

def rank_cardinality(df):
    """
    Takes a dataframe and returns it's column names 
    listed in order of increasing cardinality
    Params:
        df (pandas DataFrame)
    
    Returns:
        List of df column names from lowest cardinality to highest cardinality.
    """

    cat_columns = df.select_dtypes(exclude='number')
    perc_unique = {}
    for col in cat_columns:
        pu = df[col].nunique() / df.shape[0]
        perc_unique.update({col: pu})
        
    # sort using the 2nd element in unique.items()
    sorted_tups = sorted(perc_unique.items(), key=lambda x: x[1])
    column_names_sorted = [tup[0] for tup in sorted_tups]

    return column_names_sorted

    



def cardinality_report(df):
    """
    Takes a dataframe and returns a report on the cardinality
    of categorical columns within the dataframe
    Params:
        df (pandas DataFrame)
    
    Returns:
        A series of 4 Print Statements for each Categorical Column
        identified in the dataframe separated by a newline
        The ouptut is ordered from lowest cardinality to 
        highest cardinality variables
    """
    # Get only categorical features from DF
    # Apply Ranking Function
    ranked_categoricals = rank_cardinality(df)
    
    # Evaluate cardinality qualities for each feature
    for i, col in enumerate(ranked_categoricals):
        print('-------------')
        print(f"COLUMN: {col}")
        print(f"nUnique: {df[col].nunique()}")
        print("--- TOP 5 ---")
        print(df[col].value_counts().nlargest(5))
        print('\n')
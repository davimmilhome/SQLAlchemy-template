""""""
import sys

import pandas as pd

from cfg.database import connection
from scripts.queries.querie_example import function_querie_example
from scripts.python.script_example import dataframe_work_example


def data_extract_example():
    """
    Docstring
    """
    try:
        result_data = pd.read_sql_query(function_querie_example(), connection)
        data_modified = dataframe_work_example(result_data)
        
        data_modified.to_csv(
            "output/example_file.csv",
            index=False,
            sep=";",
            header=False,
            decimal=','
        )

    except Exception as e:
        print("[LOG-SQL-ERRO]: Message: " + str(e))
        sys.exit()


if __name__ == '__main__':
    data_extract_example()

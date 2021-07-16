import pandas as pd 
from pandasql import sqldf 

class FileParser: 
    
    def read_file_to_dataframe(self):
        df = pd.read_csv(self.file_directory, 
                              delimiter=self.column_delimiter, 
                              skiprows=self.skip_rows, 
                              skipfooter=self.skip_last_rows,
                              header=None,
                              nrows=self.limit_rows)
        
        df.columns = [f"c{index + 1}" for index, _ in enumerate(df.columns)]
        self.df = df
    
    def execute_sql_in_dataframe(self, query):
        file = self.df
        return sqldf(query, locals())
    
    def __init__(self, file_directory, column_delimiter, skip_rows = 0, skip_last_rows = 0, limit_rows = None):
        self.file_directory = file_directory
        self.column_delimiter = column_delimiter
        self.skip_rows = skip_rows
        self.skip_last_rows = skip_last_rows
        self.limit_rows = None if limit_rows == 0 else limit_rows
        self.df = None
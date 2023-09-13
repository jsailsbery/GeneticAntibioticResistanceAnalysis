import pandas as pd
from typing import List, Union
import warnings

class DataFrameHandler:
    @staticmethod
    def read_csv_data(file_path: str) -> Union[pd.DataFrame, None]:
        """
        Read data from a CSV file and return it as a DataFrame.

        Parameters:
            file_path (str): The path to the CSV file to read.

        Returns:
            pd.DataFrame or None: A DataFrame containing the data from the CSV file,
            or None if an error occurs during reading.
        """
        try:
            # Read the CSV file into a DataFrame with the first column as the index
            df = pd.read_csv(file_path, index_col=0)
            
            # Reset the index to make 'Sample_ID' a regular column
            df.reset_index(inplace=True)

            # Display the first few rows of the DataFrame to verify the import
            # print(df.head())

            return df
        
        except FileNotFoundError:
            print("Error: The specified file was not found.")
        except pd.errors.EmptyDataError:
            print("Error: The CSV file appears to be empty.")
        except (ValueError, TypeError) as e:
            print(f"Error: Incorrect data types in the CSV file. {str(e)}")
        
        return None

    @staticmethod
    def select_columns_by_search_terms(df: pd.DataFrame, search_terms: List[str]) -> List[str]:
        """
        Select columns from a DataFrame based on specified search terms.

        Parameters:
            df (pd.DataFrame): The DataFrame containing the data.
            search_terms (List[str]): List of search terms to find matching columns.

        Returns:
            selected_columns (List[str]): List of column names that match any of the search terms.
        """
        try:
            if not isinstance(df, pd.DataFrame):
                raise ValueError("The 'df' parameter must be a pandas DataFrame.")

            if not isinstance(search_terms, list):
                raise ValueError("The 'search_terms' parameter must be a list of strings.")

            selected_columns = []

            for search_term in search_terms:
                if not isinstance(search_term, str):
                    raise ValueError("Each search term in 'search_terms' must be a string.")

                matching_columns = [col for col in df.columns if search_term.lower() in col.lower()]
                selected_columns.extend(matching_columns)

            if not selected_columns:
                warnings.warn("No columns matched the provided search terms.", UserWarning)

            return selected_columns

        except ValueError as ve:
            print(f"ValueError: {str(ve)}")
            return []

    @staticmethod
    def add_data_to_dataframe(df: pd.DataFrame, new_data: dict) -> pd.DataFrame:
        """
        Add new data to an existing DataFrame.

        Parameters:
            df (pd.DataFrame): The DataFrame to which new data should be added.
            new_data (dict): A dictionary containing new data to be added, where keys are column names
                             and values are lists of data to add.

        Returns:
            pd.DataFrame: The DataFrame with the new data added.
        """
        try:
            if not isinstance(df, pd.DataFrame):
                raise ValueError("The 'df' parameter must be a pandas DataFrame.")

            if not isinstance(new_data, dict):
                raise ValueError("The 'new_data' parameter must be a dictionary.")

            for col_name, data in new_data.items():
                if col_name in df.columns:
                    raise ValueError(f"Column '{col_name}' already found in the DataFrame.")

                if len(data) != len(df):
                    raise ValueError(f"The length of the data for '{col_name}' should match the DataFrame.")

                df[col_name] = data

            return df

        except ValueError as ve:
            print(f"ValueError: {str(ve)}")
            return df

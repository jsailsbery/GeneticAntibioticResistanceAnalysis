import unittest
import pandas as pd
from functions.data_frame_handler import DataFrameHandler  # Adjust this import path as needed

class TestDataFrameHandler(unittest.TestCase):
    def test_add_data_to_dataframe(self):
        # Create a sample DataFrame
        data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        df = pd.DataFrame(data)

        # Define new data to add
        new_data = {'C': [7, 8, 9], 'D': [10, 11, 12]}

        # Add new data to the DataFrame
        updated_df = DataFrameHandler.add_data_to_dataframe(df, new_data)

        # Verify if the new data has been added correctly
        self.assertTrue('C' in updated_df.columns)
        self.assertTrue('D' in updated_df.columns)
        self.assertEqual(list(updated_df['C']), [7, 8, 9])
        self.assertEqual(list(updated_df['D']), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()


import unittest
import pandas as pd
import os

def join_csv_files(file1, file2, key1='GEO_ID', key2='GEOIDFQ', output_file='joined.csv'):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    merged_df = df1.merge(df2, left_on=key1, right_on=key2, how='inner')
    merged_df.to_csv(output_file, index=False)
    return output_file

class TestJoinCSVFiles(unittest.TestCase):

    def setUp(self):
        """Create test CSV files with sample data."""
        self.file1 = "test1.csv"
        self.file2 = "test2.csv"
        self.output_file = "test_output.csv"

        df1 = pd.DataFrame({'GEO_ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
        df2 = pd.DataFrame({'GEOIDFQ': [2, 3, 4], 'Value': [100, 200, 300]})

        df1.to_csv(self.file1, index=False)
        df2.to_csv(self.file2, index=False)

    def test_successful_join(self):
        """Test that the function correctly joins two CSV files."""
        result_df = join_csv_files(self.file1, self.file2, key1='GEO_ID', key2='GEOIDFQ', output_file=self.output_file)

        # Expected DataFrame after the join
        expected_df = pd.DataFrame({'GEO_ID': [2, 3], 'Name': ['B', 'C'], 'GEOIDFQ': [2, 3], 'Value': [100, 200]})

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_no_common_values(self):
        """Test when there are no matching keys between the two files."""
        df1 = pd.DataFrame({'GEO_ID': [5, 6, 7], 'Name': ['X', 'Y', 'Z']})
        df2 = pd.DataFrame({'GEOIDFQ': [1, 2, 3], 'Value': [10, 20, 30]})

        df1.to_csv(self.file1, index=False)
        df2.to_csv(self.file2, index=False)

        result_df = join_csv_files(self.file1, self.file2, key1='GEO_ID', key2='GEOIDFQ', output_file=self.output_file)

        self.assertTrue(result_df.empty, "The joined DataFrame should be empty when no keys match.")

    def test_empty_file(self):
        """Test behavior when one of the input files is empty."""
        pd.DataFrame(columns=['GEO_ID', 'Name']).to_csv(self.file1, index=False)  # Empty file1
        pd.DataFrame({'GEOIDFQ': [1, 2, 3], 'Value': [10, 20, 30]}).to_csv(self.file2, index=False)

        result_df = join_csv_files(self.file1, self.file2, key1='GEO_ID', key2='GEOIDFQ', output_file=self.output_file)

        self.assertTrue(result_df.empty, "The output should be empty if one input file is empty.")

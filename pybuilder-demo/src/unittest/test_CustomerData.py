import unittest
import pandas as pd
from unittest.mock import patch, mock_open
from io import StringIO

class CustomerData:
    def __init__(self):
        self.customers = {'Name': ['John Smith', 'Jane Doe', 'Bob Johnson'],
                 'Age': [35, 28, 42],
                 'Address': ['123 Main St', '456 Park Ave', '789 Elm St']}

    def create_dataframe(self):
        # Create a DataFrame with the customer information
        self.df = pd.DataFrame(self.customers)
        
    def save_to_csv(self, filename, index=False):
        # Save the DataFrame to a new file
        self.df.to_csv(filename, index=index)

class TestCustomerData(unittest.TestCase):
    def test_create_dataframe(self):
        # Create an instance of the CustomerData class
        data = CustomerData()
        data.create_dataframe()

        # Assert that the DataFrame has the correct number of rows
        self.assertEqual(len(data.df), 3)

        # Assert that the DataFrame has the correct columns
        self.assertEqual(list(data.df.columns), ['Name', 'Age', 'Address'])
        
    @patch('builtins.open', new_callable=mock_open)
    def test_save_to_csv(self, mock_file):
        # Create an instance of the CustomerData class
        data = CustomerData()
        data.create_dataframe()

        # Save the DataFrame to a CSV file
        data.save_to_csv('customers.csv')

        # Assert that the file was opened in write mode
        mock_file.assert_called_once_with('customers.csv', 'w')

        # Assert that the file was written with the correct DataFrame content
        expected_output = StringIO()
        data.df.to_csv(expected_output, index=False)
        mock_file().write.assert_called_once_with(expected_output.getvalue())

if __name__ == '__main__':
    unittest.main()

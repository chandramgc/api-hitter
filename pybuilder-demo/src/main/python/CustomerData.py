import pandas as pd

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

def main():
    # Create a new instance of the CustomerData class
    data = CustomerData()
    data.create_dataframe()
    data.save_to_csv('customers.csv')

if __name__ == '__main__':
    main()

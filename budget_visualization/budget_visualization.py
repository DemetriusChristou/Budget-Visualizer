import pandas as pd
import constant

#Main function
def main():
    df = read_user_csv_into_data_frame()

    
    #get income
    #get expenses
    #get avg spent per day (would need to parse the first and last Date column to figure out how many days this covers)

    sum_of_transactions = df[constant.AMOUNT_COLUMN].sum()
    print("sum of transactions:", round(sum_of_transactions, 2))


#Read csv input from user into a df 
def read_user_csv_into_data_frame():
    while True:
        filePath = 'C:\\Users\\deema\\source\\repos\\Budget-Visualizer\\data\\May2022.csv'
        #input("Csv file path to analyize.\n")

        try:
            return pd.read_csv(filePath)
        except FileNotFoundError:
            print("Invalid file path try again\n")

if __name__ == "__main__":
    main()
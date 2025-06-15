#Gregory Mah 041114855
#CST 8002 020 Programming Language Research Proj
#Stanley Pieda
#Due 2025-05-25


#Main method to run the program
if __name__ == "__main__":

    """Print my my name on to terminal so it is always visible"""
    print("Gregory Mah 041114855")

    """Set records array to hold value returned by CSVReader method"""
    records = CSVReader(csvData)

    """Loop through and print the list of objects"""
    for record in records:
        print(record)
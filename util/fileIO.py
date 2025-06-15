#Gregory Mah 041114855
#CST 8002 020 Programming Language Research Proj
#Stanley Pieda
#Due 2025-06-13

#Import csv and record to read dataset and to store records as Record objects to be read.
import csv
import model.Record as Record

#Variable to store name of dataset file to be used to access file
csvData = "Nitrogen oxide emissions by facility.csv"

#Method to handle CSV reading using the variable csvData with dataset name
def CSVReader(csvData):
    """Initialize array to store record objects from the dataset"""
    records = []

    try:
        """Open CSV file using csvData variable"""
        with open(csvData) as file:

            """Create reader variable to use csv Dictionary Reader to read CSV"""
            reader = csv.DictReader(file)

            """Loop through dataset and track how many records are read"""
            for dataSet, row in enumerate(reader):

                """Use only a few records as per assignment instructions"""
                if dataSet >= 100:
                    break

                """Instantiate record object for current iteration of loop"""
                record = Record.Record(
                    NPRID = row["NPRI ID"], facility = row["Facility name"], company = row["Company name"], 
                    address = row["Address"], city = row["City"], province = row["Province"], postal = row["PostalCode"], 
                    lat = row["Latitude"], long = row["Longitude"], emissions = row["Emissions"], units = row["Units"], 
                    details = row["Facility details"], info = row["Facility information"], year = row["Report year"]
                )

                """Add new record to records array"""
                records.append(record)

    #Exception handling for file not found with error message
    except FileNotFoundError:
        print("File could not be located")

    #Exception handling for other exceptions    
    except Exception as e:
        print(f"ERROR: {e}")
        
    #Return records array after being populated
    return records

def CSVSaver(record, csvData):

    try: 
    
        with open (csvData, mode ='w') as file:
        
            writer = csv.writer(file)

            writer.writerow([
                "NPRI ID", "Facility name", "Company name", "Address", "City", "Province", "PostalCode", 
                "Latitude", "Longitude", "Emissions", "Units", "Facility details", "Facility information",
                "Report year"
            ])

            for record in records:
                writer.writerow([
                    record.NPRID, record.facility, record.company, record.address, record.city, record.province,
                    record.postal, record.lat, record.long, record.emissions, record.units, record.details,
                    record.info, record.year
                ])

    except Exception as error:
        print(f"ERROR: Cannot write to file: {error}")
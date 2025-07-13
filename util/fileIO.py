"""
Gregory Mah 041114855
CST 8002 020 Programming Language Research Proj
Stanley Pieda
Due 2025-06-15

Import csv and record to read dataset and to store records as Record objects to be read.
"""

import csv
import uuid
from pathlib import Path
from typing import List
import model.Record as Record

class FileRepository:
    #Variable to store name of dataset file to be used to access file
    csvData = "data/Nitrogen oxide emissions by facility.csv"

    #Method to handle CSV reading using the variable csvData with dataset name
    def CSVReader(csvData):
        """
        Initialize array to store record objects from the dataset
        
        Parameters:
        csvData (str): CSV file path.

        Returns:
        A list of Record objects.
        """
        records = []

        try:
            """Open CSV file using csvData variable"""
            with open(csvData, newline='') as file:

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

    def CSVSaver(self, records: List[Record]):
        """
        Saves record objects to a new CSV file with a randomly generated UUID file name.

        Parameters:
            records (list): List of Record objects stored in memory from CSV file.
            csvData (str): CSV file path.
        """

        try: 
        
            outfile = self.filename.parent / f"output_{uuid.uuid4()}.csv"
            with outfile.open (mode ='w', newline='') as file:
            
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
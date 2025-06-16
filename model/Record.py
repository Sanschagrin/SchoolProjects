"""
Model Class: Record.py
Author: Gregory Mah (041114855)
Course: CST 8002 020 Programming Language Research Project
Due Date: 2025-06-15

This class designs the model to be used as the data access object to interact with the database and the controller.
"""

class Record:
    """This is the record class that will represent objects from the Nitrogen oxide emissions by facility dataset."""

    #This method signified by the 'def' keyword or defined. It is the constructor for the record class and allows records to be instantiated
    def __init__(self, NPRID, facility, company, address, city, province, postal, lat, long, emissions, units, details, info, year):
        """A list of Parameters from the data set with matching variables to hold their values in the object"""
        """
        Initializes a Record instance.

        Parameters:
            NPRID (str): NPRI ID.
            facility (str): Facility name.
            company (str): Company name.
            address (str): Street address.
            city (str): City.
            province (str): Province.
            postal (str): Postal code.
            lat (str): Latitude.
            long (str): Longitude.
            emissions (str): Emission amount.
            units (str): Emission units.
            details (str): Facility details.
            info (str): Additional info.
            year (str): Report year.
        """
        self.NPRID = NPRID
        self.facility = facility
        self.company = company
        self.address = address
        self.city = city
        self.province = province
        self.postal = postal
        self.lat = lat
        self.long = long
        self.emissions = emissions
        self.units = units
        self.details = details
        self.info = info
        self.year = year
    
    def __str__(self):
        """String method to return record object in the form of a string."""
        return f"NPRID: {self.NPRID}, {self.facility}, {self.company}, {self.address}, {self.city}, {self.province}, {self.postal}, {self.lat}, {self.long},  {self.emissions}, {self.units}, {self.details}, {self.info}, {self.year}"
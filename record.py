#Gregory Mah 041114855
#CST 8002 020 Programming Language Research Proj
#Stanley Pieda
#Due 2025-05-25

#This is the record class that will represent objects from the Nitrogen oxide emissions by facility dataset.
class Record:

    #This method signified by the 'def' keyword or defined. It is the constructor for the record class and allows records to be instantiated
    def __init__(self, NPRID, facility, company, address, city, province, postal, lat, long, emissions, units, details, info, year):
        #A list of Parameters from the data set with matching variables to hold their values in the object
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
    
    #String method to return record object in the form of a string.
    def __str__(self):
        return f"NPRID: {self.NPRID}, {self.facility}, {self.company}, {self.address}, {self.city}, {self.province}, {self.postal}, {self.lat}, {self.long},  {self.emissions}, {self.units}, {self.details}, {self.info}, {self.year}"
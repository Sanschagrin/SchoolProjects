
class Record:
    def __init__(self, NPRID=0, facility="", company="", address="", city="", province="", postal="", lat=0.0, long=0.0, emissions="", units="", details="", info="", year=0):
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
        return f"NPRID: {self.NPRID}, {self.facility}, {self.company}, {self.address}, {self.city}, {self.province}, {self.postal}, {self.lat}, {self.long},  {self.emissions}, {self.units}, {self.details}, {self.info}, {self.year}"
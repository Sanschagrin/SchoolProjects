#Gregory Mah 041114855
#CST 8002 020 Programming Language Research Proj
#Stanley Pieda
#Due 2025-06-14

def welcome(me = "Gregory Mah 41114855"):
    print(f"Welcome to the menu")
    print(f"By {me}\n")

def menu():
    print("Menu")
    print("1. Reload file")
    print("2. Select single record")
    print("3. Select multiple records")
    print("4. Create new record ")
    print("5. Edit a record")
    print("6. Delete a record")
    print("7. Save data to new file")

def userID():
    return input("Enter NPRIID of your selected record")

def allRecords(records):
    if not records:
        print("File is empty")
        return
    for record in records:
        print(record)

def newRecord():
    print("Enter record details below")
    return {
        "NPRID": input("NPRIID: "), "facility": input("Facility: "), "company": input("Company: "), 
        "address": input("Address: "), "city": input("City: "), "province": input("Province: "), 
        "postal": input("Postal Code: "), "lat": input("Latitude: "), "long": input("Longitude: "), 
        "emissions": input("Emission Type: "), "units": input("Emission Units: "), "details": input("Details: "),
        "info": input("Information: "), "year": input("Year")

    }

def displayRecord(record):
    print("Record Details")
    print (record)

def message(msg):
    print(f"Information: {msg}"
    )

def error(msg):
    print(f"ERROR: {msg}"
          )
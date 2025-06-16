#Gregory Mah 041114855
#CST 8002 020 Programming Language Research Proj
#Stanley Pieda
#Due 2025-06-14

def welcome(me = "Gregory Mah 41114855"):
    print(f"Welcome to the menu")
    print(f"By {me}\n")

def menu():
    print("Menu")
    print("1. Reload file: ")
    print("2. Select single record: ")
    print("3. Select multiple records: ")
    print("4. Create new record: ")
    print("5. Edit a record: ")
    print("6. Delete a record: ")
    print("7. Save data to new file: ")

def userID():
    return input("Enter NPRIID of your selected record: ")

def allRecords(records):
    if not records:
        print("File is empty")
        return
    for record in records:
        print(record)

def newRecord(editing=False, old_record=None):
    print("Enter record details below: ")
    return {
        "NPRID": input("NPRIID: ") or (old_record.NPRID if editing else ""),
        "facility": input("Facility: ") or (old_record.facility if editing else ""),
        "company": input("Company: ") or (old_record.company if editing else ""),
        "address": input("Address: ") or (old_record.address if editing else ""),
        "city": input("City: ") or (old_record.city if editing else ""),
        "province": input("Province: ") or (old_record.province if editing else ""),
        "postal": input("Postal Code: ") or (old_record.postal if editing else ""),
        "lat": input("Latitude: ") or (old_record.lat if editing else ""),
        "long": input("Longitude: ") or (old_record.long if editing else ""),
        "emissions": input("Emission Type: ") or (old_record.emissions if editing else ""),
        "units": input("Emission Units: ") or (old_record.units if editing else ""),
        "details": input("Details: ") or (old_record.details if editing else ""),
        "info": input("Information: ") or (old_record.info if editing else ""),
        "year": input("Year: ") or (old_record.year if editing else ""),
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
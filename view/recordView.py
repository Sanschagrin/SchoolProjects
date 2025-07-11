"""
View: recordView.py
Author: Gregory Mah (041114855)
Course: CST 8002 020 Programming Language Research Project
Instructor: Stanley Pieda
Due Date: 2025-06-15

Used to create input/output view logic to the user interface and get input.
"""
class recordView: 

    def welcome(me = "Gregory Mah 41114855"):
        """
        Print welcome message.
        """
        print(f"Welcome to the menu")
        print(f"By {me}\n")

    def menu():
        """
        Display user options to user to prompt user input.
        """
        print("Menu")
        print("1. Reload file: ")
        print("2. Select single record: ")
        print("3. Select multiple records: ")
        print("4. Create new record: ")
        print("5. Edit a record: ")
        print("6. Delete a record: ")
        print("7. Save data to new file: ")

    def userID():
        """
        Display prompt for NPRIID for identifying a record.
        
        Returns:
            STR: NPRIID inputted by user.
        """
        return input("Enter NPRIID of your selected record: ")

    def allRecords(records):
        """
        Print many records.

        Parameters:
            records (list): List of objects from memory list.
        """
        if not records:
            print("File is empty")
            return
        for record in records:
            print(record)

    def newRecord(editing=False, old_record=None):
        """
        Display prompt to edit or create record.

        Parameters:
            editing (boolean): flag to indicate this as a editing or creation operation.
            old_record (Record): record values for editing existing fields.
    .
        """
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
        """
        Print single Record.

        Parameters:
            record (Record): record object.
        """
        print("Record Details")
        print (record)

    def message(msg):
        """
        Print message regarding operation.

        Parameters:
            msg (str): displayed message.
        """
        print(f"Information: {msg}"
        )

    def error(msg):
        """
        Print error message regarding operation.

        Parameters:
            msg (str): displayed error.
        """
        print(f"ERROR: {msg}"
            )
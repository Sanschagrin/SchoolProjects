"""
Controller: recordController.py
Author: Gregory Mah (041114855)
Course: CST 8002 020 Programming Language Research Project
Instructor: Stanley Pieda
Due Date: 2025-06-15

This class is the controller that handles logic for reading, creating, editing,
deleting, and saving records using the Record model. Anything that requires interaction with
the database is validated here.
"""

from model.Record import Record
from view.recordView import displayRecord, allRecords, message, error, newRecord, userID
from util.fileIO import CSVReader, CSVSaver
import uuid

class recordController:
    """
    Class to control Record objects and their interactions with the view/model.
    """
    def __init__(self):
        """
        Initialize controller with Nitrogen CSV file and empty list.
        """
        self.filename = "data/Nitrogen oxide emissions by facility.csv"
        self.records = []

    def reloadData(self):
        """
        Reload CSV file data using CSVReader method.
        """
        self.records = CSVReader(self.filename)
        message("Data Reloaded")

    def saveData(self):
        """
        Save data to a file with a UUID name using CSVSaver.
        """
        new_filename = f"data/output_{uuid.uuid4()}.csv"
        CSVSaver(self.records, new_filename)
        message(f"Data saved to {new_filename}")

    def displaySingleRecord(self):
        """
        Display single record using inputed NPRIID.
        """
        NPRIID = userID().strip()
        data = next((r for r in self.records if str(r.NPRID).strip() == NPRIID), None)
        if data:
            displayRecord(data)
        else:
            error("Record not found.")

    def displayAllRecords(self):
        """
        Display many records using the view and fileIO.
        """
        allRecords(self.records)

    def createRecord(self):
        """
        Get input to fill fields and add a record to the list.
        """
        newData = newRecord()
        record = Record(**newData)
        self.records.append(record)
        message("Record added.")

    def editRecord(self):
        """
        Edit existing records based on inputted NPRIID.
        """
        NPRIID = userID().strip()
        record = next((r for r in self.records if str(r.NPRID).strip() == NPRIID), None)
        if record:
            updated_data = newRecord(editing=True, old_record=record)
            for key, value in updated_data.items():
                setattr(record, key, value)
            message("Record updated.")
        else:
            error("Record not found.")

    def deleteRecord(self):
        """
        Delete existing records based on inputted NPRIID.
        """
        NPRIID = userID().strip()
        record = next((r for r in self.records if str(r.NPRID).strip() == NPRIID), None)
        if record:
            self.records.remove(record)
            message("Record deleted.")
        else:
            error("Record not found.")
#Gregory Mah 041114855
#CST 8002 020 Programming Language Research Proj
#Stanley Pieda
#Due 2025-06-15

from model.Record import Record
from view.recordView import displayRecord, allRecords, message, error, newRecord, userID
from util.fileIO import CSVReader, CSVSaver
import uuid

class recordController:
    def __init__(self):
        self.filename = "data/Nitrogen oxide emissions by facility.csv"
        self.records = []

    def reloadData(self):
        self.records = CSVReader(self.filename)
        message("Data Reloaded")

    def saveData(self):
        new_filename = f"data/output_{uuid.uuid4()}.csv"
        CSVSaver(self.records, new_filename)
        message(f"Data saved to {new_filename}")

    def displaySingleRecord(self):
        NPRIID = userID()
        data = next((r for r in self.records if r.NPRID == NPRIID), None)
        if data:
            displayRecord(data)
        else:
            error("Record not found.")

    def displayAllRecords(self):
        allRecords(self.records)

    def createRecord(self):
        newData = newRecord()
        record = Record(**newData)
        self.records.append(record)
        message("Record added.")

    
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
from typing import List, Optional, Protocol
from model.Record import Record
from view.recordView import RecordView
from util.fileIO import CSVReader, CSVSaver
import uuid

class RepositoryProtocol(Protocol):
    """Narrow controller expectations"""

    def load_records(self) -> List[Record]: ...

    def insert_record(self, record: Record) -> None: ...

    def update_record(self, record: Record) -> bool: ...

    def delete_record(self, npri_id: str) -> bool: ...

class recordController:
    """
    Class to control Record objects and their interactions with the view/model.
    """
    def __init__(self, repo: RepositoryProtocol, view: RecordView):
        """
        Initialize controller with Nitrogen CSV file and empty list.
        """
        self.repo = repo
        self.view = view
        self.records: List[Record] = []

        def run(self):  
            self.reload_data()
            self.view.show_welcome()

            while True:
                self.view.show_menu()
                match self.view.get_choice():
                    case "1":
                        self.reload_data()
                    case "2":
                        self.display_single()
                    case "3":
                        self.display_all()
                    case "4":
                        self.create()
                    case "5":
                        self.edit()
                    case "6":
                        self.delete()
                    case "q":
                        self.view.info("Goodbye!")
                        break
                    case _:
                        self.view.error("Invalid option.")

    def reloadData(self):
        """
        Reload CSV file data using CSVReader method.
        """
        self.records = self.repo.load_records()
        self.view.info("Data Reloaded")



    def _find_in_memory(self, npri_id: str) -> Optional[Record]:
        return next((r for r in self.records if r.NPRID == npri_id), None)

    def displaySingleRecord(self):
        """
        Display single record using inputed NPRIID.
        """
        npri = self.view.prompt_npri_id()
        rec = self._find_in_memory(npri)
        if rec:
            self.view.display_record(rec)
        else:
            self.view.error("Record not found.")

    def displayAllRecords(self):
        """
        Display many records using the view and fileIO.
        """
        self.view.display_records(self.records)

    def createRecord(self):
        """
        Get input to fill fields and add a record to the list.
        """
        data = self.view.prompt_record()
        rec = Record(**data)
        try:
            self.repo.insert_record(rec)
            self.records.append(rec) 
            self.view.info("Record added to database.")
        except Exception as exc:  
            self.view.error(str(exc))

    def editRecord(self):
        """
        Edit existing records based on inputted NPRIID.
        """
        npri = self.view.prompt_npri_id()
        rec = self._find_in_memory(npri)
        if not rec:
            self.view.error("Record not found.")
            return
        updates = self.view.prompt_record(editing=True, old=rec)
        for k, v in updates.items():
            setattr(rec, k, v)
        if self.repo.update_record(rec):
            self.view.info("Record updated.")
        else:
            self.view.error("Update failed – check NPRID.")

    def deleteRecord(self):
        """
        Delete existing records based on inputted NPRIID.
        """
        npri = self.view.prompt_npri_id()
        if self.repo.delete_record(npri):
            self.records = [r for r in self.records if r.NPRID != npri]
            self.view.info("Record deleted.")
        else:
            self.view.error("Delete failed – NPRID not found.")
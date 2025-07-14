"""
View: recordView.py
Author: Gregory Mah (041114855)
Course: CST 8002 020 Programming Language Research Project
Instructor: Stanley Pieda
Due Date: 2025-06-15

Used to create input/output view logic to the user interface and get input.
"""

from typing import List, Optional

from model.Record import Record


class RecordView:
    """Console view layer"""

    def __init__(self, author: str = "Gregory Mah 041114855") -> None:
        """
        Initialization method to display Author name.
        """
        self.author = author


    def show_welcome(self): 
        """
        Method used to display welcome message.
        """
        print(f"Welcome to the Nitrogen-Oxide Records App — {self.author}\n")

    def show_menu(self): 
        """
        Method used to display options for user interactions.
        """
        print("\n===============================")
        print(self.author)
        print("===============================")
        print("1  Reload from database")
        print("2  Display a single record")
        print("3  Display ALL records")
        print("4  Create a new record")
        print("5  Edit a record")
        print("6  Delete a record")
        print("q  Quit")

    @staticmethod
    def get_choice() -> str:
        """
        Method used to get input from user.
        """
        return input("\nEnter choice: ").strip().lower()

    @staticmethod
    def prompt_npri_id() -> str:
        """
        Method used to display prompt for NPRIID and to get user input.
        """
        return input("Enter NPRI ID: ").strip()

    def prompt_record(self, *, editing: bool = False, old: Optional[Record] = None) -> dict[str, str]:
        """
        Display prompt to edit or create record.

        Parameters:
            editing (boolean): flag to indicate this as a editing or creation operation.
            old_record (Record): record values for editing existing fields.
    .
        """
        def _ask(label: str, default: str = "") -> str:
            prompt = f"{label} [{default}]: " if editing else f"{label}: "
            return input(prompt).strip() or default

        return {
            "NPRID": _ask("NPRI ID", old.NPRID if editing and old else ""),
            "facility": _ask("Facility", old.facility if editing and old else ""),
            "company": _ask("Company", old.company if editing and old else ""),
            "address": _ask("Address", old.address if editing and old else ""),
            "city": _ask("City", old.city if editing and old else ""),
            "province": _ask("Province", old.province if editing and old else ""),
            "postal": _ask("Postal", old.postal if editing and old else ""),
            "lat": _ask("Latitude", old.lat if editing and old else ""),
            "long": _ask("Longitude", old.long if editing and old else ""),
            "emissions": _ask("Emissions", old.emissions if editing and old else ""),
            "units": _ask("Units", old.units if editing and old else ""),
            "details": _ask("Details", old.details if editing and old else ""),
            "info": _ask("Info", old.info if editing and old else ""),
            "year": _ask("Year", old.year if editing and old else ""),
        }

    @staticmethod
    def display_record(rec: Record):
        """
        Print single Record.

        Parameters:
            record (Record): record object.
        """
        print("\nRecord Details")
        print(rec)

    @staticmethod
    def display_records(records: List[Record]):
        """
        Print the record list to the user.

        Parameters:
            records (List[Record]): List of records saved to be displayed.
        """
        if not records:
            print("No records available.")
            return
        for rec in records:
            print(rec)
    """
    Print message regarding operation.

    Parameters:
        msg (str): displayed message.
    """
    @staticmethod
    def info(msg: str):
        print(f"INFO: {msg}")
    """
    Print error message regarding operation.

    Parameters:
        msg (str): displayed error.
    """
    @staticmethod
    def error(msg: str):
        print(f"ERROR: {msg}")
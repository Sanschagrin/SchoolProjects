"""
Main Runner: methodMain.py
Author: Gregory Mah (041114855)
Course: CST 8002 020 Programming Language Research Project
Instructor: Stanley Pieda
Due Date: 2025-06-15

This class acts as the main entry point for the application, to interact with the controller.
"""
from util.database_repository import DatabaseRepository
from controller.recordController import RecordController
from view.recordView import RecordView
from util.file_repository import FileRepository

def main():
    """
    Main method that starts the application. It initilizes the controller, view and repositories. 

    If database is empty is empty it will load the CSV data into the database.
    """
    repo = DatabaseRepository("data/emissions.db", max_records=None)
    view = RecordView()

    if not repo.load_records():
        print("Database empty – seeding from CSV …")
        from util.file_repository import FileRepository

        seed_records = FileRepository("data/Nitrogen oxide emissions by facility.csv", max_records=None).load_records()
        repo.save_records(seed_records)
        print("Seed complete.\n")

    RecordController(repo, view).run()

if __name__ == "__main__":
    main()

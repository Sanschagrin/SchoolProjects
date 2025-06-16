"""
Main Runner: methodMain.py
Author: Gregory Mah (041114855)
Course: CST 8002 020 Programming Language Research Project
Instructor: Stanley Pieda
Due Date: 2025-06-15

This class acts as the main entry point for the application, to interact with the controller.
"""
from controller.recordController import recordController
from view.recordView import menu, message, error

def main():
    """
    Main method to begin the application.
    """
    controller = recordController()
    controller.reloadData()

    while True:
        print("\n===============================")
        print("Gregory Mah 041114855")  # Always show name
        print("===============================\n")
        menu()

        choice = input("\nEnter your choice (1-7, or q to quit): ").strip().lower()

        if choice == "1":
            controller.reloadData()
        elif choice == "2":
            controller.displaySingleRecord()
        elif choice == "3":
            controller.displayAllRecords()
        elif choice == "4":
            controller.createRecord()
        elif choice == "5":
            controller.editRecord()
        elif choice == "6":
            controller.deleteRecord()
        elif choice == "7":
            controller.saveData()
        elif choice == "q":
            message("Exiting program. Goodbye!")
            break
        else:
            error("Invalid option. Please enter a number between 1-7 or 'q' to quit.")

if __name__ == "__main__":
    main()

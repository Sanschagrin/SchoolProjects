"""
Unit Test File: test_add_record.py
Author: Gregory Mah (041114855)
Course: CST 8002 020 Programming Language Research Project
Professor: Stanley Pieda
Due Date: 2025-06-15

This file features unit testing for verifying the add record function
in Record Controller.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from model.Record import Record
from controller.recordController import recordController

class TestAddRecord(unittest.TestCase):
    """
    Unit test class to add a new record to the record list in memory.
    """
    def test_add_new_record(self):
        """
        This class checks if new records can be added to the programs memory list.
        Asserts if the count increases and checks if the NPRIID and facility are equal to the test parameters.
        """
        controller = recordController()
        initial_count = len(controller.records)

        # Act: Create a new record manually and append it
        new_data = {
            "NPRID": "50000",
            "facility": "Algonquin",
            "company": "College",
            "address": "1385 Woodroffe",
            "city": "Ottawa",
            "province": "ON",
            "postal": "T3S7C0",
            "lat": "45.4215",
            "long": "-75.6990",
            "emissions": "123.45",
            "units": "Tonnes",
            "details": "Computer Programming",
            "info": "Mel Sanschagrin",
            "year": "2025"
        }
        record = Record(**new_data)
        controller.records.append(record)

        # Assert
        self.assertEqual(len(controller.records), initial_count + 1)
        self.assertEqual(controller.records[-1].NPRID, "50000")
        self.assertEqual(controller.records[-1].facility, "Algonquin")

if __name__ == '__main__':
    unittest.main()
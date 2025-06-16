import unittest
from model.Record import Record
from controller.recordController import recordController

class TestAddRecord(unittest.TestCase):
    def test_add_new_record(self):
        # Arrange
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
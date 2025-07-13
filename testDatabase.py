"""
Unit Test File: testDatabase.py
Author: Gregory Mah (041114855)
Course: CST 8002 020 Programming Language Research Project
Professor: Stanley Pieda
Due Date: 2025-07-13

This file features unit testing for verifying the database is being utilized
"""
import unittest

from model.Record import Record
from util.database_repository import DatabaseRepository


class TestDatabase(unittest.TestCase):
    """Basic CRUD test on an in‑memory SQLite DB."""

    def setUp(self):
        # Each test gets a fresh, in‑memory database
        self.repo = DatabaseRepository("file::memory:?cache=shared", max_records=None)

    # ---------- insert + load ----------
    def test_insert_and_load(self):
        rec = Record(
            NPRID="40000",
            facility="Tuna",
            company="Fish Inc.",
            address="1385 Tuna Way",
            city="Ottawa",
            province="ON",
            postal="T7N4F1S4",
            lat="100",
            long="100",
            emissions="tonnes",
            units="fish",
            details="Tuna",
            info="Tuna",
            year="2024",
        )
        self.repo.insert_record(rec)

        loaded = self.repo.load_records()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].NPRID, "40000")

    def test_update_and_delete(self):
        rec = Record(
            NPRID="50000",
            facility="Salmon Facility",
            company="Fish Ltd.",
            address="8513 Salmon St.",
            city="Fish",
            province="ON",
            postal="S4L3ON",
            lat="10",
            long="10",
            emissions="Tonnes",
            units="Salmons",
            details="Fishes",
            info="Fish",
            year="2025",
        )
        self.repo.insert_record(rec)

        # --- update ---
        rec.facility = "Updated Facility"
        self.assertTrue(self.repo.update_record(rec))

        reloaded = self.repo.load_records()
        self.assertEqual(reloaded[0].facility, "Tuna")

        # --- delete ---
        self.assertTrue(self.repo.delete_record("50000"))
        self.assertTrue(self.repo.delete_record("40000"))
        self.assertEqual(len(self.repo.load_records()), 0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

"""
Model Class: Record.py
Author: Gregory Mah (041114855)
Course: CST 8002 020 Programming Language Research Project
Due Date: 2025-06-15

This class designs the model to be used as the data access object to interact with the database and the controller.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class Record:
    """This is the record class that will represent objects from the Nitrogen oxide emissions by facility dataset."""

    NPRID: str
    facility: str
    company: str
    address: str
    city: str
    province: str
    postal: str
    lat: str
    long: str
    emissions: str
    units: str
    details: str
    info: str
    year: str

    def __str__(self) -> str:
        """String method to return record object in the form of a string."""
        return (
        f"NPRID: {self.NPRID}, Facility: {self.facility}, Company: {self.company}, "
        f"Address: {self.address}, City: {self.city}, Province: {self.province}, "
        f"Postal: {self.postal}, Lat: {self.lat}, Long: {self.long}, "
        f"Emissions: {self.emissions} {self.units}, Details: {self.details}, "
        f"Info: {self.info}, Year: {self.year}"
        )
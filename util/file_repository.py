import csv
import uuid
from pathlib import Path
from typing import List, Optional

from model.Record import Record


class FileRepository:

    """
    Handles loading and saving emission records to/from a CSV file for the database to save.

    Attributes:
        filename (Path): Indicates the path used to locate CSV file.
        max_records (Optional[int]): Inticates that all records are to be saved for the database to load.
    """
    
    HEADERS = [
        "NPRI ID",
        "Facility name",
        "Company name",
        "Address",
        "City",
        "Province",
        "PostalCode",
        "Latitude",
        "Longitude",
        "Emissions",
        "Units",
        "Facility details",
        "Facility information",
        "Report year",
    ]

    def __init__(self, filename: str | Path, max_records: Optional[int] = None):
        """
        Initialization method for file repository class.

        Args:
            filename (str | Path): Indicates the path used to locate CSV file.
            max_records (Optional[int]): Inticates that all records are to be saved for the database to load.
        """
        self.filename = Path(filename)
        self.max_records = max_records 

    def load_records(self) -> List[Record]:
        """
        Loads CSV file records to be added to database

        Returns:
            List[Record]: List of the row records in the CSV.
        """
        records: List[Record] = []
        with self.filename.open(newline="") as fh:
            reader = csv.DictReader(fh)
            for idx, row in enumerate(reader):
                if self.max_records is not None and idx >= self.max_records:
                    break
                records.append(
                    Record(
                        NPRID=row["NPRI ID"].strip(),
                        facility=row["Facility name"],
                        company=row["Company name"],
                        address=row["Address"],
                        city=row["City"],
                        province=row["Province"],
                        postal=row["PostalCode"],
                        lat=row["Latitude"],
                        long=row["Longitude"],
                        emissions=row["Emissions"],
                        units=row["Units"],
                        details=row["Facility details"],
                        info=row["Facility information"],
                        year=row["Report year"],
                    )
                )
        return records

    def save_records(self, records: List[Record]):
        """
        Saves records and creates a new CSV file to store them in with generated UUID file name

        Args:
            records (List[Record]): List of the row records in the CSV.

        Returns:
            Path: Indicates the path used to locate the new CSV file.
        """
        outfile = self.filename.parent / f"output_{uuid.uuid4()}.csv"
        with outfile.open("w", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(self.HEADERS)
            for r in records:
                writer.writerow([
                    r.NPRID,
                    r.facility,
                    r.company,
                    r.address,
                    r.city,
                    r.province,
                    r.postal,
                    r.lat,
                    r.long,
                    r.emissions,
                    r.units,
                    r.details,
                    r.info,
                    r.year,
                ])
        return outfile

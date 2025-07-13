import csv
import uuid
from pathlib import Path
from typing import List, Optional

from model.Record import Record


class FileRepository:
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
        self.filename = Path(filename)
        self.max_records = max_records  # None ⇒ no limit

    def load_records(self) -> List[Record]:
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

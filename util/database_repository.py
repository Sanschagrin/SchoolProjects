from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable, List, Optional

from model.Record import Record


class DatabaseRepository:
    """SQLite table creation

    Creates table on launch and handles CRUD operations
    """

    TABLE_NAME = "emissions"

    def __init__(self, db_path: str | Path, *, max_records: Optional[int] = None):
        self.db_path = Path(db_path)
        self.max_records = max_records
        self._ensure_table()


    def load_records(self) -> List[Record]:
        with self._connect() as con:
            sql = f"SELECT * FROM {self.TABLE_NAME}"
            params: tuple = ()
            if self.max_records is not None:
                sql += " LIMIT ?"
                params = (self.max_records,)
            cur = con.execute(sql, params)
            return [self._row_to_record(row) for row in cur.fetchall()]

    def insert_record(self, record: Record) -> None:
        with self._connect() as con:
            con.execute(
                f"""
                INSERT INTO {self.TABLE_NAME} (
                    NPRID, facility, company, address, city, province, postal,
                    lat, long, emissions, units, details, info, year
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                self._record_to_tuple(record),
            )

    def update_record(self, record: Record) -> bool:
        with self._connect() as con:
            cur = con.execute(
                f"""
                UPDATE {self.TABLE_NAME}
                SET facility=?, company=?, address=?, city=?, province=?, postal=?,
                    lat=?, long=?, emissions=?, units=?, details=?, info=?, year=?
                WHERE NPRID=?
                """,
                (
                    record.facility,
                    record.company,
                    record.address,
                    record.city,
                    record.province,
                    record.postal,
                    record.lat,
                    record.long,
                    record.emissions,
                    record.units,
                    record.details,
                    record.info,
                    record.year,
                    record.NPRID,
                ),
            )
            return cur.rowcount > 0

    def delete_record(self, npri_id: str) -> bool:
        with self._connect() as con:
            cur = con.execute(
                f"DELETE FROM {self.TABLE_NAME} WHERE NPRID = ?", (npri_id,)
            )
            return cur.rowcount > 0

    # bulk‑write helper – overwrite table contents (rarely needed now)
    def save_records(self, records: Iterable[Record]) -> None:
        with self._connect() as con:
            con.execute(f"DELETE FROM {self.TABLE_NAME}")
            con.executemany(
                f"""
                INSERT INTO {self.TABLE_NAME} (
                    NPRID, facility, company, address, city, province, postal,
                    lat, long, emissions, units, details, info, year
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (self._record_to_tuple(r) for r in records),
            )

    # ---------- internal helpers ----------
    def _connect(self):
        return sqlite3.connect(self.db_path, uri=True)

    def _ensure_table(self) -> None:
        with self._connect() as con:
            con.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                    NPRID TEXT PRIMARY KEY,
                    facility TEXT,
                    company TEXT,
                    address TEXT,
                    city TEXT,
                    province TEXT,
                    postal TEXT,
                    lat TEXT,
                    long TEXT,
                    emissions TEXT,
                    units TEXT,
                    details TEXT,
                    info TEXT,
                    year TEXT
                )
                """
            )

    @staticmethod
    def _row_to_record(row: sqlite3.Row | tuple) -> Record:
        return Record(
            NPRID=row[0],
            facility=row[1],
            company=row[2],
            address=row[3],
            city=row[4],
            province=row[5],
            postal=row[6],
            lat=row[7],
            long=row[8],
            emissions=row[9],
            units=row[10],
            details=row[11],
            info=row[12],
            year=row[13],
        )

    @staticmethod
    def _record_to_tuple(record: Record) -> tuple:
        return (
            record.NPRID,
            record.facility,
            record.company,
            record.address,
            record.city,
            record.province,
            record.postal,
            record.lat,
            record.long,
            record.emissions,
            record.units,
            record.details,
            record.info,
            record.year,
        )
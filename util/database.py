import sqlite3
from contextlib import closing
from model.Record import Record       

class FileRepository:

    DB_NAME = "data/emissions.db"


    def _get_conn():
        """Return a new connection with rows as dict‑like objects."""
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row     
        return conn


    def init_schema() -> None:
        """Create the table once (called at start‑up)."""
        with closing(_get_conn()) as conn, conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS emissions (
                    NPRID     TEXT PRIMARY KEY,
                    facility  TEXT,
                    company   TEXT,
                    address   TEXT,
                    city      TEXT,
                    province  TEXT,
                    postal    TEXT,
                    lat       REAL,
                    long      REAL,
                    emissions REAL,
                    units     TEXT,
                    details   TEXT,
                    info      TEXT,
                    year      INTEGER
                );
            """)



    def insert(record: Record) -> None:
        """Insert a new Record (raises sqlite3.IntegrityError if NPRID exists)."""
        with closing(_get_conn()) as conn, conn:
            conn.execute("""
                INSERT INTO emissions VALUES
                (:NPRID, :facility, :company, :address, :city, :province, :postal,
                :lat, :long, :emissions, :units, :details, :info, :year)
            """, vars(record))                       

    def fetch_one(nprid: str) -> Record | None:
        with closing(_get_conn()) as conn:
            row = conn.execute(
                "SELECT * FROM emissions WHERE NPRID = ?", (nprid,)
            ).fetchone()
            return Record(**row) if row else None


    def fetch_all() -> list[Record]:
        with closing(_get_conn()) as conn:
            rows = conn.execute("SELECT * FROM emissions").fetchall()
        return [Record(**row) for row in rows]


    def update(record: Record) -> bool:
        with closing(_get_conn()) as conn, conn:
            cur = conn.execute("""
                UPDATE emissions SET
                facility=:facility, company=:company, address=:address,
                city=:city, province=:province, postal=:postal,
                lat=:lat, long=:long, emissions=:emissions, units=:units,
                details=:details, info=:info, year=:year
                WHERE NPRID=:NPRID
            """, vars(record))
            return cur.rowcount == 1               


    def delete(nprid: str) -> bool:
        with closing(_get_conn()) as conn, conn:
            cur = conn.execute("DELETE FROM emissions WHERE NPRID = ?", (nprid,))
            return cur.rowcount == 1
        
        # util/database.py  (append below the other code)

    def import_csv_once(csv_path: str) -> None:
        """
        Populate the DB the first time the program runs.
        Does nothing if the table already contains rows.
        """
        if fetch_all():          # table already has data
            return

        from util.fileIO import CSVReader
        for record in CSVReader(csv_path):
            try:
                insert(record)
            except sqlite3.IntegrityError:
                pass            # skip duplicates
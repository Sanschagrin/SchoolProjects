CREATE TABLE IF NOT EXISTS emissions (
    NPRID          TEXT PRIMARY KEY,
    facility       TEXT,
    company        TEXT,
    address        TEXT,
    city           TEXT,
    province       TEXT,         
    postal         TEXT,
    lat            TEXT,                  
    long           TEXT,
    emissions      TEXT,                  
    units          TEXT,                  
    details        TEXT,
    info           TEXT,
    year           TEXT                   
);
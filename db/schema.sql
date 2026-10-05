DROP TABLE IF EXISTS results;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS drivers;

CREATE TABLE drivers (
    name_acronym TEXT PRIMARY KEY,
    full_name    TEXT NOT NULL
);

CREATE TABLE sessions (
    session_key        INTEGER PRIMARY KEY,
    meeting_key        INTEGER,
    session_name       TEXT NOT NULL,
    session_year       INTEGER NOT NULL,
    session_date       DATE,
    circuit_short_name TEXT
);

CREATE TABLE results (
    session_key    INTEGER NOT NULL REFERENCES sessions(session_key),
    name_acronym   TEXT    NOT NULL REFERENCES drivers(name_acronym),
    driver_number  INTEGER NOT NULL,
    team_name      TEXT,
    position       INTEGER,
    points         NUMERIC,
    number_of_laps INTEGER,
    dnf            BOOLEAN,
    dns            BOOLEAN,
    dsq            BOOLEAN,
    duration       NUMERIC,
    gap_to_leader  TEXT,
    PRIMARY KEY (session_key, name_acronym)
);
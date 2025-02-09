import sqlite3

conn = sqlite3.connect('alumni_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tbl_alumni (
    aid_pk INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_url TEXT UNIQUE NOT NULL
    aalumni TEXT NOT NULL,
    alocation TEXT,
    amajor TEXT,
    agraduation_year  TEXT,
    ajob_title TEXT,
    acertificate TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tbl_school (
    sid_pk INTEGER PRIMARY KEY AUTOINCREMENT,
    aid_fk INTEGER,
    suniversity_name TEXT,
    suniversity_major TEXT,
    suniversity_location TEXT,
    suniversity_start DATE,
    suniversity_end DATE,
    FOREIGN KEY (aid_fk) REFERENCES tbl_alumni(aid_pk)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tbl_experience (
    eid_pk INTEGER PRIMARY KEY AUTOINCREMENT,
    aid_fk INTEGER,
    etitle TEXT,
    ecompany_name TEXT,
    ecompany_location TEXT,
    ecompany_size INTEGER,
    etitle_start DATE,
    etitle_end DATE,
    FOREIGN KEY (aid_fk) REFERENCES tbl_alumni(aid_pk)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tbl_location (
    lid_pk INTEGER PRIMARY KEY AUTOINCREMENT,
    aid_fk INTEGER,
    lcountry TEXT,
    lstate TEXT,
    lzip INTEGER,
    lcity TEXT,
    FOREIGN KEY (aid_fk) REFERENCES tbl_alumni(aid_pk)
);
''')

conn.commit()
conn.close()

print("Alumni schema has been created.")

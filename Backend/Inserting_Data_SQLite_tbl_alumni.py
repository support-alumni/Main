import sqlite3

TABLE_NAME = "tbl_alumni"
COLUMN_NAMES = "(profile_url, aalumni, alocation, amajor, agraduation_year, ajob_title, acertificate)"

def insert_alumni(profile_url, name, location, major, graduation_year,
                  job_title, certificate,db_name='alumni_database.db'):
    sql_query = f'''
        INSERT INTO {TABLE_NAME} {COLUMN_NAMES}
        VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_query, (profile_url, name, location, major,
                            graduation_year, job_title, certificate))
    except sqlite3.IntegrityError as e:
        print(f"Error inserting {name}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

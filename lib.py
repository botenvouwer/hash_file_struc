import sqlite3
import hashlib
import json


def extract_file_structure(geopackage_path):
    # create a connection to the SQLite file
    conn = sqlite3.connect(geopackage_path)

    # get a cursor object to execute SQL commands
    cur = conn.cursor()

    # query the SQLite master table for all table names
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # initialize an empty dictionary to store the file structure
    file_structure = {}

    # iterate over the table names and get their column names
    for table_name in cur.fetchall():
        table_name = table_name[0]
        cur.execute(f"PRAGMA table_info({table_name});")
        columns = [col[1] for col in cur.fetchall()]
        file_structure[table_name] = columns

    # close the cursor and the connection
    cur.close()
    conn.close()

    return file_structure


def hash_file_structure(geopackage_path):
    file_structure = extract_file_structure(geopackage_path)
    json_file_structure = json.dumps(file_structure, sort_keys=True)
    file_hash = hashlib.md5(json_file_structure.encode("utf-8")).hexdigest()

    return file_hash

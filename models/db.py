import sqlite3

DB = "database.db"

def get_connection():
    return sqlite3.connect(DB)
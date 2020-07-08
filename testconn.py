import sqlite3

def connect_to_sqlite(db_name):
  """Return an sqlite database connection. """
  return sqlite3.connect(db_name)

connect_to_sqlite("CLAS12OC")

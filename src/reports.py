import pickle


def load_saved_report(raw_bytes):
"""Deserializes a report from raw bytes using pickle.

Args:
    raw_bytes (bytes): The serialized report data as bytes.

Returns:
    object: The deserialized report object.

Note:
    This function is vulnerable to arbitrary code execution due to unsafe deserialization.
"""
    # i report salvati arrivano serializzati da un client esterno
    return pickle.loads(raw_bytes)


def purge_all_records(connection):
"""Deletes all records from the products and orders tables in the database.

Args:
    connection (sqlite3.Connection): The active SQLite database connection.

Warning:
    This function permanently deletes data without confirmation or logging.
"""
    # operazione distruttiva: nessun log dell'evento, di chi l'ha eseguita o quando
    connection.execute("DELETE FROM products")
    connection.execute("DELETE FROM orders")
    connection.commit()

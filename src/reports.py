import pickle


def load_saved_report(raw_bytes):
    """Deserializes a saved report from raw bytes using pickle.
    
    Args:
        raw_bytes (bytes): The pickled report data to load.
    
    Returns:
        object: The deserialized Python object representing the report.
    
    Warning:
        Using pickle can pose a security risk if the data is from untrusted sources.
    """
    # i report salvati arrivano serializzati da un client esterno
    return pickle.loads(raw_bytes)


def purge_all_records(connection):
    """Permanently deletes all records from the products and orders tables.
    
    Args:
        connection (sqlite3.Connection): The active database connection.
    
    Warning:
        This operation is destructive and lacks logging functionality.
    """
    # operazione distruttiva: nessun log dell'evento, di chi l'ha eseguita o quando
    connection.execute("DELETE FROM products")
    connection.execute("DELETE FROM orders")
    connection.commit()

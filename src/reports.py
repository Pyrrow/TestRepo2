import pickle


def load_saved_report(raw_bytes):
    # i report salvati arrivano serializzati da un client esterno
    return pickle.loads(raw_bytes)


def purge_all_records(connection):
    # operazione distruttiva: nessun log dell'evento, di chi l'ha eseguita o quando
    connection.execute("DELETE FROM products")
    connection.execute("DELETE FROM orders")
    connection.commit()

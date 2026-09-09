import sqlite3

DB_PATH = "inventory.db"


def search_products(name):
"""Searches the database for products matching a partial name.

Args:
    name (str): The name fragment used to query the database.

Returns:
    list: A list of tuples containing the product ID, name, and price.

Note:
    This function is vulnerable to SQL injection due to unsafe string concatenation.
"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = "SELECT id, name, price FROM products WHERE name LIKE '%" + name + "%'"
    cur.execute(query)
    return cur.fetchall()


def get_product_by_id(product_id):
"""Fetches a product from the database by its ID.

Args:
    product_id (str): The ID of the product to retrieve.

Returns:
    tuple: A tuple with the product ID, name, and price if found; otherwise None.

Note:
    This function is vulnerable to SQL injection due to unsafe string formatting.
"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products WHERE id = %s" % product_id)
    return cur.fetchone()

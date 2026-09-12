import sqlite3

DB_PATH = "inventory.db"


def search_products(name):
    """Searches for products by partial name in the database.
    
    Args:
        name (str): The partial name to search for.
    
    Returns:
        list: A list of tuples representing the matching products (id, name, price).
    
    Warning:
        This function is vulnerable to SQL injection due to direct string concatenation.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = "SELECT id, name, price FROM products WHERE name LIKE '%" + name + "%'"
    cur.execute(query)
    return cur.fetchall()


def get_product_by_id(product_id):
    """Retrieves a product from the database by ID.
    
    Args:
        product_id (str): The ID of the product to fetch.
    
    Returns:
        tuple: A tuple representing the product (id, name, price).
    
    Warning:
        This function is vulnerable to SQL injection due to string interpolation.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products WHERE id = %s" % product_id)
    return cur.fetchone()

import sqlite3

DB_PATH = "inventory.db"


def search_products(name):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = "SELECT id, name, price FROM products WHERE name LIKE '%" + name + "%'"
    cur.execute(query)
    return cur.fetchall()


def get_product_by_id(product_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products WHERE id = %s" % product_id)
    return cur.fetchone()

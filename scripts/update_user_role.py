import sqlite3


def run():
    conn = sqlite3.connect("healthcare.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET role = 'admin' WHERE username = 'adarshgzz'")
    conn.commit()
    print(f"Updated {cursor.rowcount} rows. adarshgzz is now an admin.")
    conn.close()

if __name__ == "__main__":
    run()

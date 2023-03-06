import sqlite3


def init():
    """
    Used to seed the jobs database with fake test data, should only have 1 entry
    """

    sql_script = None

    with open("schema.sql", "r") as sql_file:
        sql_script = sql_file.read()
    db = sqlite3.connect("jobs.db")
    cursor = db.cursor()
    cursor.executescript(sql_script)

    db.commit()
    db.close()


if __name__ == "__main__":
    init()

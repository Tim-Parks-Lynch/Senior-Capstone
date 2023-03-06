import sqlite3

QUERY = "SELECT * FROM jobs;"


def main():
    con = sqlite3.connect("jobs.db")
    cur = con.cursor()

    cur.execute(QUERY)
    row = cur.fetchall()
    print(row)


if __name__ == "__main__":
    main()

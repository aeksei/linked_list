import sqlite3


class DBConnection:
    def __init__(self, database):
        self.database = database
        self.sqliteConnection = sqlite3.connect(self.database)
        print("Successfully Connected to SQLite")
        self.cursor = None

    def __enter__(self):
        self.cursor = self.sqliteConnection.cursor()

        return self.cursor

    # except
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            print("Failed")
            self.sqliteConnection.rollback()
        else:
            print("Success")
            self.sqliteConnection.commit()


        #     except sqlite3.Error as error:
        #     print("Error while creating a sqlite table", error)
        #
        # finally:
        # if (sqliteConnection):
        #     sqliteConnection.close()
        #     print("sqlite connection is closed")


if __name__ == '__main__':
    db = DBConnection('test.db')

    with db as cursor:
        sql_update_query = """CREATE TABLE IF NOT EXISTS test"""
        cursor.execute(sql_update_query)
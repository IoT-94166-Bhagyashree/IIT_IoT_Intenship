import mysql.connector


def getBDConnection():
    connection = mysql.connector.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        password = "root",
        database = "smart_agriculture",
        use_pure = True
    )

    return connection
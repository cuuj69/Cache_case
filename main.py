import sqlite3

def get_my_friends():
    connection = sqlite3.connect(database="database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT Id, name FROM users;")
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    return result

if __name__ == '__main__':
    print(get_my_friends())
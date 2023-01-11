import sqlite3
import json
import redis


def get_my_friends():
    connection = sqlite3.connect(database="database.db")
    cursor = connection.cursor()
    redis_client =redis.Redis()

    cached_friends = redis_client.get('user_friends')
    if cached_friends is not None:
        return json.dumps(cached_friends)


    cursor.execute("SELECT Id, name FROM users;")
    cursor.execute("DROP TABLE  users;")
    result = cursor.fetchall()

    redis_client.set(name='user_friends', value=json.duresult)

    cursor.close()
    connection.close()
    redis_client.close()
    return result

if __name__ == '__main__':
    print(get_my_friends())
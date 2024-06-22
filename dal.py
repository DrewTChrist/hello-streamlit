from psycopg2 import pool
from psycopg2.errors import UniqueViolation

def create_user(URL, name, player_id, api_key) -> int | None:
    user_id_created = None

    connection_pool = pool.SimpleConnectionPool(1, 10, URL)

    connection = connection_pool.getconn()

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users (name, torn_id, api_key) VALUES (%s, %s, %s) RETURNING id;", 
        (name, player_id, api_key)
    )

    user_id_created = cursor.fetchone()[0]

    cursor.close()

    connection.commit()

    connection_pool.putconn(connection)

    connection_pool.closeall()

    return user_id_created

def create_settings(URL, user_id):
    connection_pool = pool.SimpleConnectionPool(1, 10, URL)

    connection = connection_pool.getconn()

    cursor = connection.cursor()

    settings_id_created = cursor.execute(
        "INSERT INTO settings (user_id, show_plushies, show_flowers, show_meds, show_boosters) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
        (user_id, True, True, True, True)
    )

    connection.commit()

    connection_pool.putconn(connection)

    connection_pool.closeall()

    return settings_id_created

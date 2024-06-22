from psycopg2 import pool

def create_user(URL, name, player_id, api_key):
    connection_pool = pool.SimpleConnectionPool(1, 10, URL)

    connection = connection_pool.getconn()

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users (name, torn_id, api_key) VALUES (%s, %s, %s)", 
        (name, player_id, api_key)
    )

    cursor.close()

    connection.commit()

    connection_pool.putconn(connection)

    connection_pool.closeall()
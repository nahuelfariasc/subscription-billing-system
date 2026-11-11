from database.config_db import connect


def save_client(name, last_name, email):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO client (name, last_name, email) VALUES (%s, %s, %s) RETURNING id",
        (name, last_name, email),
    )
    client_id = cursor.fetchone()[0]
    conexion.commit()
    cursor.close()
    conexion.close()
    return client_id


def get_clients():
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, name, last_name, email FROM client")
    rows = cursor.fetchall()
    cursor.close()
    conexion.close()
    return rows


def get_client(client_id):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT id, name, last_name, email FROM client WHERE id = %s",
        (client_id,),
    )
    row = cursor.fetchone()
    cursor.close()
    conexion.close()
    return row


def update_client(client_id, name, last_name, email):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE client SET name = %s, last_name = %s, email = %s WHERE id = %s",
        (name, last_name, email, client_id),
    )
    conexion.commit()
    cursor.close()
    conexion.close()


def delete_client(client_id):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM client WHERE id = %s", (client_id,))
    conexion.commit()
    cursor.close()
    conexion.close()

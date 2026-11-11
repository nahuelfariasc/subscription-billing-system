from database.config_db import connect


def save_subscription(client_id, plan_id, date_start, date_end, status, cancellation_requested=False):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO subscription (client_id, plan_id, date_start, date_end, status, cancellation_requested) "
        "VALUES (%s, %s, %s, %s, %s, %s) RETURNING id",
        (client_id, plan_id, date_start, date_end, status, cancellation_requested),
    )
    sub_id = cursor.fetchone()[0]
    conexion.commit()
    cursor.close()
    conexion.close()
    return sub_id


def get_subscriptions():
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT id, client_id, plan_id, date_start, date_end, status, cancellation_requested FROM subscription"
    )
    rows = cursor.fetchall()
    cursor.close()
    conexion.close()
    return rows


def get_subscription(sub_id):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT id, client_id, plan_id, date_start, date_end, status, cancellation_requested "
        "FROM subscription WHERE id = %s",
        (sub_id,),
    )
    row = cursor.fetchone()
    cursor.close()
    conexion.close()
    return row


def update_subscription(sub_id, client_id, plan_id, date_start, date_end, status, cancellation_requested):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE subscription SET client_id = %s, plan_id = %s, date_start = %s, date_end = %s, "
        "status = %s, cancellation_requested = %s WHERE id = %s",
        (client_id, plan_id, date_start, date_end, status, cancellation_requested, sub_id),
    )
    conexion.commit()
    cursor.close()
    conexion.close()


def delete_subscription(sub_id):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM subscription WHERE id = %s", (sub_id,))
    conexion.commit()
    cursor.close()
    conexion.close()

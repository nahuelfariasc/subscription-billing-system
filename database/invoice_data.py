from database.config_db import connect


def save_invoice(client_id, broadcast, expiration, amount, status):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO invoice (client_id, broadcast, expiration, amount, status) "
        "VALUES (%s, %s, %s, %s, %s) RETURNING id",
        (client_id, broadcast, expiration, amount, status),
    )
    invoice_id = cursor.fetchone()[0]
    conexion.commit()
    cursor.close()
    conexion.close()
    return invoice_id


def get_invoices():
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, client_id, broadcast, expiration, amount, status FROM invoice")
    rows = cursor.fetchall()
    cursor.close()
    conexion.close()
    return rows


def get_invoice(invoice_id):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT id, client_id, broadcast, expiration, amount, status FROM invoice WHERE id = %s",
        (invoice_id,),
    )
    row = cursor.fetchone()
    cursor.close()
    conexion.close()
    return row


def update_invoice(invoice_id, client_id, broadcast, expiration, amount, status):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE invoice SET client_id = %s, broadcast = %s, expiration = %s, amount = %s, status = %s WHERE id = %s",
        (client_id, broadcast, expiration, amount, status, invoice_id),
    )
    conexion.commit()
    cursor.close()
    conexion.close()


def delete_invoice(invoice_id):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM invoice WHERE id = %s", (invoice_id,))
    conexion.commit()
    cursor.close()
    conexion.close()

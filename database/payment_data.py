from database.config_db import connect


def save_payment(invoice_id, pay_date, amount, method, status):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO payment (invoice_id, date, amount, method, status) "
        "VALUES (%s, %s, %s, %s, %s) RETURNING id",
        (invoice_id, pay_date, amount, method, status),
    )
    payment_id = cursor.fetchone()[0]
    conexion.commit()
    cursor.close()
    conexion.close()
    return payment_id


def get_payments():
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, invoice_id, date, amount, method, status FROM payment")
    rows = cursor.fetchall()
    cursor.close()
    conexion.close()
    return rows


def get_payment(payment_id):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT id, invoice_id, date, amount, method, status FROM payment WHERE id = %s",
        (payment_id,),
    )
    row = cursor.fetchone()
    cursor.close()
    conexion.close()
    return row


def update_payment(payment_id, invoice_id, pay_date, amount, method, status):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE payment SET invoice_id = %s, date = %s, amount = %s, method = %s, status = %s WHERE id = %s",
        (invoice_id, pay_date, amount, method, status, payment_id),
    )
    conexion.commit()
    cursor.close()
    conexion.close()


def delete_payment(payment_id):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM payment WHERE id = %s", (payment_id,))
    conexion.commit()
    cursor.close()
    conexion.close()

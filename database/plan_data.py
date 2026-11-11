from database.config_db import connect


def save_plan(name, description, price, frequency, status):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO plan (name, description, price, frequency, status) "
        "VALUES (%s, %s, %s, %s, %s) RETURNING id",
        (name, description, price, frequency, status),
    )
    plan_id = cursor.fetchone()[0]
    conexion.commit()
    cursor.close()
    conexion.close()
    return plan_id


def get_plans():
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, name, description, price, frequency, status FROM plan")
    rows = cursor.fetchall()
    cursor.close()
    conexion.close()
    return rows


def get_plan(plan_id):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT id, name, description, price, frequency, status FROM plan WHERE id = %s",
        (plan_id,),
    )
    row = cursor.fetchone()
    cursor.close()
    conexion.close()
    return row


def update_plan(plan_id, name, description, price, frequency, status):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE plan SET name = %s, description = %s, price = %s, frequency = %s, status = %s WHERE id = %s",
        (name, description, price, frequency, status, plan_id),
    )
    conexion.commit()
    cursor.close()
    conexion.close()


def delete_plan(plan_id):
    conexion = connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM plan WHERE id = %s", (plan_id,))
    conexion.commit()
    cursor.close()
    conexion.close()

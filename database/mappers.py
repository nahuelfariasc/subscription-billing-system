from models.client import Client
from models.invoice import Invoice
from models.payment import Payment
from models.plan import Plan
from models.subscription import Subscription


def row_to_client(row):
    # row: (id, name, last_name, email)
    return Client(row[1], row[2], row[3])


def row_to_plan(row):
    # row: (id, name, description, price, frequency, status)
    return Plan(row[1], row[2], row[3], row[4], row[5])


def row_to_subscription(row):
    # row: (id, client_id, plan_id, date_start, date_end, status, cancellation_requested)
    # client y plan se inyectan despues si se necesitan
    sub = Subscription(row[3], row[4], row[5])
    sub.cancellation_requested = row[6]
    return sub


def row_to_invoice(row):
    # row: (id, client_id, broadcast, expiration, amount, status)
    return Invoice(row[2], row[3], row[4], row[5])


def row_to_payment(row):
    # row: (id, invoice_id, date, amount, method, status)
    pay = Payment(row[2], row[3], row[4])
    pay.status = row[5]
    return pay

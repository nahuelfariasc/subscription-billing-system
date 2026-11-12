-- Seed de datos iniciales de prueba para S&BM (PostgreSQL)

-- 1. Clientes
INSERT INTO client (name, last_name, email) VALUES
('Nahuel', 'Farias', 'nahuel@ejemplo.com'),
('Ada', 'Lovelace', 'ada@ejemplo.com'),
('Alan', 'Turing', 'alan@ejemplo.com')
ON CONFLICT (email) DO NOTHING;

-- 2. Planes
INSERT INTO plan (name, description, price, frequency, status) VALUES
('Plan Basico Mensual', 'Acceso estandar con facturacion mensual', 9.99, 'monthly', 'active'),
('Plan Premium Mensual', 'Acceso completo con facturacion mensual', 19.99, 'monthly', 'active'),
('Plan Pro Anual', 'Acceso completo con facturacion anual y descuento', 199.99, 'yearly', 'active'),
('Plan Obsoleto', 'Plan discontinuado', 5.00, 'monthly', 'inactive');

-- 3. Suscripciones (para los clientes 1 y 2 con planes 1 y 2)
INSERT INTO subscription (client_id, plan_id, date_start, date_end, status, cancellation_requested) VALUES
(1, 1, CURRENT_DATE, (CURRENT_DATE + INTERVAL '1 month')::date, 'active', FALSE),
(2, 2, CURRENT_DATE, (CURRENT_DATE + INTERVAL '1 month')::date, 'active', FALSE);

-- 4. Invoices (facturas generadas asociadas a la expiración de la suscripción)
INSERT INTO invoice (client_id, broadcast, expiration, amount, status) VALUES
(1, CURRENT_DATE, (CURRENT_DATE + INTERVAL '1 month')::date, 9.99, 'paid'),
(2, CURRENT_DATE, (CURRENT_DATE + INTERVAL '1 month')::date, 19.99, 'pending');

-- 5. Pagos (pago para la factura 1)
INSERT INTO payment (invoice_id, date, amount, method, status) VALUES
(1, CURRENT_DATE, 9.99, 'credit_card', 'completed');

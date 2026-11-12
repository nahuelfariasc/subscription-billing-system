# S&BM — Subscription & Billing Management

Sistema de gestion de suscripciones y facturacion (OOP, Python + PostgreSQL).

## Requisitos

- Python 3.10+
- PostgreSQL 14+ (local o remoto)
- Cliente SQL (psql, Beekeeper, pgAdmin, etc.)

## Instalacion

1. Clonar el repositorio.
2. Instalar dependencias (elegir una):
   ```bash
   # pip (Windows/macOS/Linux)
   pip install -r requirements.txt

   # uv (recomendado en Arch/Omarchy)
   uv pip install -r requirements.txt
   ```
3. Crear la base de datos y el usuario con tu cliente SQL preferido
   (psql, Beekeeper, pgAdmin, etc.) y ejecutar `database/schema.sql`.
4. Configurar credenciales:
   ```bash
   cp .env.example .env
   # editar .env con host, puerto, usuario, password y nombre de DB
   ```

## Uso

```bash
# con uv
uv run python main.py

# o activando el venv
source .venv/bin/activate
python main.py
```

## Tests

```bash
python -m unittest tests.test_domain tests.test_integration
```

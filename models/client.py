class Client:
    def __init__(self, c_name, c_last_name, c_email):
        if not c_name or not c_name.strip():
            raise ValueError("Name cannot be empty")
        if not c_last_name or not c_last_name.strip():
            raise ValueError("Last name cannot be empty")

        self.name = c_name
        self.last_name = c_last_name
        self.email = self._validate_email(c_email)

    def _validate_email(self, email):
        email = email.strip().lower()

        if "@" not in email:
            raise ValueError("Invalid email address")

        parts = email.split("@")

        if len(parts) != 2:
            raise ValueError("Invalid email address")

        if not parts[0] or "." not in parts[1]:
            raise ValueError("Invalid email address")

        if parts[1].startswith(".") or parts[1].endswith("."):
            raise ValueError("Invalid email address")

        return email

    def update(self, name = None, last_name = None, email = None):
        if name is not None:
            if not name.strip():
                raise ValueError("Name cannot be empty")
            self.name = name

        if last_name is not None:
            if not last_name.strip():
                raise ValueError("Last name cannot be empty")
            self.last_name = last_name

        if email is not None:
            self.email = self._validate_email(email)

# classes all go in here
#!/usr/bin/env python3
class User:
    def __init__(self, fist_name, last_name, email):
        self.first_name = fist_name
        self.last_name = last_name
        self.email = email

    def end_email(self):
        return f"{self.first_name}.{self.last_name}@{self.email}"

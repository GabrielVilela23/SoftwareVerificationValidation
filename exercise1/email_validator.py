def is_valid_email(email):
    if "@" not in email:
        return False

    username, domain = email.split("@", 1)

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    return True

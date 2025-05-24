def is_palindrome(text):
    """Sprawdza, czy dany tekst jest palindromem."""
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
def calculate_rectangle_area(width, height):
    """Zwraca pole prostokąta."""
    if width < 0 or height < 0:
        raise ValueError("Wymiary nie mogą być ujemne.")
    return width * height
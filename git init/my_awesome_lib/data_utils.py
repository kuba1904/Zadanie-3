def convert_date_format(date_str):
    """Konwertuje datę z formatu 'dd-mm-yyyy' na 'yyyy/mm/dd'."""
    from datetime import datetime
    try:
        return datetime.strptime(date_str, "%d-%m-%Y").strftime("%Y/%m/%d")
    except ValueError:
        raise ValueError("Nieprawidłowy format daty.")
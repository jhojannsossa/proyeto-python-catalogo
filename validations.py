VALID_STATUSES = {"disponible", "reservada", "vendida"}

def validate_price(price):
    try:
        numeric_price = float(price)
    except (ValueError, TypeError):
        raise ValueError("El precio debe ser un valor numérico.")
    if numeric_price <= 0:
        raise ValueError("El precio debe ser mayor que cero.")
    return numeric_price

def validate_status(status):
    if not isinstance(status, str) or status.strip().lower() not in VALID_STATUSES:
        raise ValueError(f"Estado inválido. Debe ser uno de: {', '.join(VALID_STATUSES)}")
    return status.strip().lower()

def validate_description(description):
    if not isinstance(description, str):
        raise ValueError("La descripción debe ser un texto.")
    desc_lower = description.lower()
    if "usada" not in desc_lower and "certificada" not in desc_lower:
        raise ValueError("La descripción debe contener obligatoriamente la palabra 'usada' o 'certificada'.")
    return description.strip()

def validate_not_empty(value, field_name):
    if value is None or str(value).strip() == "":
        raise ValueError(f"El campo '{field_name}' no puede estar vacío.")
    return str(value).strip()
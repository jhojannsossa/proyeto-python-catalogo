from validations import (
    validate_price,
    validate_status,
    validate_description,
    validate_not_empty
)


def add_piece(id, name, category, price, status, description):
    clean_id = validate_not_empty(id, "id")
    clean_name = validate_not_empty(name, "name")
    clean_category = validate_not_empty(category, "category")
    clean_price = validate_price(price)
    clean_status = validate_status(status)
    clean_desc = validate_description(description)

    return {
        "id": clean_id,
        "name": clean_name,
        "category": clean_category,
        "price": clean_price,
        "status": clean_status,
        "description": clean_desc
    }


def list_pieces(catalog):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    if not catalog:
        return []
    return [piece["name"] for piece in catalog]


def find_piece_by_id(catalog, piece_id):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    for piece in catalog:
        if piece["id"] == piece_id:
            return piece
    return None


def remove_piece(catalog, piece_id):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    piece = find_piece_by_id(catalog, piece_id)
    if piece is None:
        raise ValueError(f"La pieza con id '{piece_id}' no fue encontrada.")

    try:
        catalog.remove(piece)
        return True
    except Exception:
        return False


def get_catalog_summary(catalog):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    summary = {}
    for piece in catalog:
        cat = piece["category"]
        summary[cat] = summary.get(cat, 0) + 1
    return summary


def get_pieces_by_category(catalog, category):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    return [piece["name"] for piece in catalog if piece["category"].lower() == category.lower()]


def piece_exists(catalog, piece_id):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    return find_piece_by_id(catalog, piece_id) is not None


def filter_by_status(catalog, status):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    valid_status = validate_status(status)
    return [piece for piece in catalog if piece["status"] == valid_status]


def filter_by_min_price(catalog, min_price):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    try:
        numeric_min = float(min_price)
    except (ValueError, TypeError):
        raise ValueError("El precio mínimo debe ser un valor numérico.")
    return [piece for piece in catalog if piece["price"] > numeric_min]


def get_average_price(catalog):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    if not catalog:
        return 0.0
    total = sum(piece["price"] for piece in catalog)
    return total / len(catalog)

def update_piece(catalog, piece_id, name=None, category=None, price=None, status=None, description=None):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    piece = find_piece_by_id(catalog, piece_id)
    if piece is None:
        raise ValueError(f"La pieza con id '{piece_id}' no fue encontrada.")

    # Si el usuario envía un nuevo valor, lo validamos y lo actualizamos
    if name is not None and name.strip() != "":
        piece["name"] = validate_not_empty(name, "name")

    if category is not None and category.strip() != "":
        piece["category"] = validate_not_empty(category, "category")

    if price is not None and str(price).strip() != "":
        piece["price"] = validate_price(price)

    if status is not None and status.strip() != "":
        piece["status"] = validate_status(status)

    if description is not None and description.strip() != "":
        piece["description"] = validate_description(description)

    return piece
import catalog as cat_mod


def mostrar_menu():
    print("\n--- GESTIÓN DE CATÁLOGO DE COLECCIONABLES ---")
    print("1. Agregar una pieza")
    print("2. Mostrar todas las piezas")
    print("3. Mostrar piezas disponibles")
    print("4. Mostrar el precio promedio")
    print("5. Buscar una pieza por identificador")
    print("6. Editar una pieza")
    print("7. Eliminar una pieza")
    print("8. Salir")


def main():
    catalog = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ").strip()

        if opcion == "1":
            print("\n--- Agregar Nueva Pieza ---")
            try:
                p_id = input("ID: ")
                p_name = input("Nombre: ")
                p_category = input("Categoría: ")
                p_price = input("Precio: ")
                p_status = input("Estado (disponible/reservada/vendida): ")
                p_desc = input("Descripción (debe incluir 'usada' o 'certificada'): ")

                new_piece = cat_mod.add_piece(p_id, p_name, p_category, p_price, p_status, p_desc)

                if cat_mod.piece_exists(catalog, new_piece["id"]):
                    print(f"Error: Ya existe una pieza con el ID '{new_piece['id']}'.")
                else:
                    catalog.append(new_piece)
                    print("¡Pieza agregada con éxito!")
            except ValueError as e:
                print(f"Error de validación: {e}")

        elif opcion == "2":
            print("\n--- Lista de Piezas ---")
            try:
                names = cat_mod.list_pieces(catalog)
                if not names:
                    print("El catálogo está vacío.")
                else:
                    for idx, name in enumerate(names, 1):
                        print(f"{idx}. {name}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "3":
            print("\n--- Piezas Disponibles ---")
            try:
                available = cat_mod.filter_by_status(catalog, "disponible")
                if not available:
                    print("No hay piezas disponibles.")
                else:
                    for p in available:
                        print(f"- ID: {p['id']} | Nombre: {p['name']} | Precio: ${p['price']:.2f}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            print("\n--- Precio Promedio ---")
            try:
                avg = cat_mod.get_average_price(catalog)
                print(f"El precio promedio del catálogo es: ${avg:.2f}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "5":
            print("\n--- Buscar Pieza por ID ---")
            try:
                search_id = input("Ingresa el ID de la pieza: ")
                piece = cat_mod.find_piece_by_id(catalog, search_id)
                if piece:
                    print("\n¡Pieza encontrada!")
                    for k, v in piece.items():
                        print(f"  {k}: {v}")
                else:
                    print("No se encontró ninguna pieza con ese identificador.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "6":
            print("\n--- Editar Pieza ---")
            try:
                search_id = input("Ingresa el ID de la pieza que deseas editar: ")
                piece = cat_mod.find_piece_by_id(catalog, search_id)
                if not piece:
                    print("No se encontró ninguna pieza con ese identificador.")
                    continue

                print(f"\nEditando pieza: {piece['name']} (Presiona Enter si no deseas cambiar un valor)")

                nuevo_nombre = input(f"Nuevo nombre [{piece['name']}]: ")
                nueva_categoria = input(f"Nueva categoría [{piece['category']}]: ")
                nuevo_precio = input(f"Nuevo precio [{piece['price']}]: ")
                nuevo_estado = input(f"Nuevo estado [{piece['status']}]: ")
                nueva_desc = input(f"Nueva descripción [{piece['description']}]: ")

                cat_mod.update_piece(
                    catalog,
                    search_id,
                    name=nuevo_nombre if nuevo_nombre else None,
                    category=nueva_categoria if nueva_categoria else None,
                    price=nuevo_precio if nuevo_precio else None,
                    status=nuevo_estado if nuevo_estado else None,
                    description=nueva_desc if nueva_desc else None
                )
                print("¡Pieza actualizada con éxito!")

            except ValueError as e:
                print(f"Error de validación: {e}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "7":
            print("\n--- Eliminar Pieza ---")
            try:
                del_id = input("Ingresa el ID de la pieza a eliminar: ")
                success = cat_mod.remove_piece(catalog, del_id)
                if success:
                    print("¡Pieza eliminada correctamente!")
            except ValueError as e:
                print(f"No se pudo eliminar: {e}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "8":  # <--- Y la opción de salir pasa a ser la 8
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona un número entre 1 y 7.")


if __name__ == "__main__":
    main()
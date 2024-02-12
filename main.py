

# Lista para almacenar los registros de usuarios
usuarios = []
# Contador global para IDs
contador_ids = 0

def new_user():
    global contador_ids
    cantidad_usuarios = int(input("\n¿Cuántos usuarios vas a registrar? "))
    
    for _ in range(cantidad_usuarios):
        contador_ids += 1
        print(f"\nIngrese los datos para el usuario {contador_ids}:")
        
        # Ingresar el nombre
        while True:
            name = input("Ingrese su(s) nombre(s):\n")
            if 5 <= len(name) <= 50:
                break
            else:
                print("Error: El nombre debe tener entre 5 y 50 caracteres. Inténtelo nuevamente.")
        
        # Ingresar los apellidos
        while True:
            last_name = input("Ingrese sus apellidos:\n")
            if 5 <= len(last_name) <= 50:
                break
            else:
                print("Error: Los apellidos deben tener entre 5 y 50 caracteres. Inténtelo nuevamente.")
        
        # Ingresar el número de teléfono
        while True:
            phone_number = input("Ingrese su número de teléfono:\n")
            if len(phone_number) == 10 and phone_number.isdigit():
                break
            else:
                print("Error: El número de teléfono debe tener exactamente 10 dígitos. Inténtelo nuevamente.")
        
        # Ingresar el correo electrónico
        while True:
            user_email = input("Ingrese su correo electrónico:\n")
            if 5 <= len(user_email) <= 50 and '@' in user_email and '.' in user_email:
                break
            else:
                print("Error: Ingrese un correo electrónico válido (entre 5 y 50 caracteres). Inténtelo nuevamente.")
        
        # Almacenar el registro del usuario en la lista como un diccionario
        usuario = {
            "ID": contador_ids,
            "Nombre": name,
            "Apellidos": last_name,
            "Teléfono": phone_number,
            "Correo": user_email
        }
        usuarios.append(usuario)
        
    print("\nRegistro completado.")

def show_user(id_usuario):
    # Ver información de un usuario por ID
    usuario_encontrado = next((usuario for usuario in usuarios if usuario["ID"] == id_usuario), None)
    if usuario_encontrado:
        print(f"\nInformación del Usuario {id_usuario}:")
        print(f"ID: {usuario_encontrado['ID']} - Nombre: {usuario_encontrado['Nombre']} {usuario_encontrado['Apellidos']} - Teléfono: {usuario_encontrado['Teléfono']} - Correo: {usuario_encontrado['Correo']}")
    else:
        print(f"No se encontró un usuario con el ID {id_usuario}.")

def edit_user(id_usuario):
    # Editar información de un usuario por ID
    usuario_encontrado = next((usuario for usuario in usuarios if usuario["ID"] == id_usuario), None)
    if usuario_encontrado:
        print(f"\nEditar Información del Usuario {id_usuario}:")

        # Ingresar el nombre
        while True:
            name = input("Ingrese su(s) nombre(s):\n")
            if 5 <= len(name) <= 50:
                break
            else:
                print("Error: El nombre debe tener entre 5 y 50 caracteres. Inténtelo nuevamente.")
        usuario_encontrado["Nombre"] = name

        # Ingresar los apellidos
        while True:
            last_name = input("Ingrese sus apellidos:\n")
            if 5 <= len(last_name) <= 50:
                break
            else:
                print("Error: Los apellidos deben tener entre 5 y 50 caracteres. Inténtelo nuevamente.")
        usuario_encontrado["Apellidos"] = last_name

        # Ingresar el número de teléfono
        while True:
            phone_number = input("Ingrese su número de teléfono:\n")
            if len(phone_number) == 10 and phone_number.isdigit():
                break
            else:
                print("Error: El número de teléfono debe tener exactamente 10 dígitos. Inténtelo nuevamente.")
        usuario_encontrado["Teléfono"] = phone_number

        # Ingresar el correo electrónico
        while True:
            user_email = input("Ingrese su correo electrónico:\n")
            if 5 <= len(user_email) <= 50 and '@' in user_email and '.' in user_email:
                break
            else:
                print("Error: Ingrese un correo electrónico válido (entre 5 y 50 caracteres). Inténtelo nuevamente.")
        usuario_encontrado["Correo"] = user_email

        print(f"Información del Usuario {id_usuario} actualizada.")
    else:
        print(f"No se encontró un usuario con el ID {id_usuario}.")

def delete_user(id_usuario):
    # Eliminar un usuario por ID
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario["ID"] != id_usuario]
    print(f"\nUsuario con ID {id_usuario} eliminado.")

def list_users():
    # Listar usuarios
    print("\nListado de usuarios:")
    for usuario in usuarios:
        print(f"ID: {usuario['ID']} - Nombre: {usuario['Nombre']} {usuario['Apellidos']} - Teléfono: {usuario['Teléfono']} - Correo: {usuario['Correo']}")

# Menú principal
while True:
    print("Bienvenido(a) a Reto Python")
    print("\nMenú:")
    print("A- Registrar nuevos usuarios")
    print("B- Listar usuarios")
    print("C- Ver información de un usuario por ID")
    print("D- Editar información de un usuario por ID")
    print("E- Eliminar usuario por ID")
    print("F- Salir")

    opcion = input("\nSeleccione una opción (A, B, C, D, E, F): ").upper()

    opciones = {
        "A": new_user,
        "B": list_users,
        "C": lambda: show_user(int(input("\nIngrese el ID del usuario que desea ver: "))),
        "D": lambda: edit_user(int(input("\nIngrese el ID del usuario que desea editar: "))),
        "E": lambda: delete_user(int(input("\nIngrese el ID del usuario que desea eliminar: "))),
        "F": lambda: exit("\n¡Hasta luego!")
    }

    try:
        opciones[opcion]()
    except KeyError:
        print("\nOpción no válida. Inténtelo nuevamente.")
    except ValueError:
        print("\nError: Ingrese un ID válido.")









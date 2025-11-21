from usuario import Usuario
from mensaje import Mensaje
from servidor import ServidorCorreo

servidores = []
usuarios = {}

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear servidor")
        print("2. Conectar servidores")
        print("3. Registrar usuario")
        print("4. Iniciar sesión")
        print("5. Ver conexiones de servidores")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        
        if opcion == "1":
            nombre = input("Nombre del servidor: ")
            servidor = ServidorCorreo(nombre)
            servidores.append(servidor)
            print(f"Servidor '{nombre}' creado exitosamente.")

        
        elif opcion == "2":
            if len(servidores) < 2:
                print("Necesita al menos dos servidores para conectar.")
                continue

            print("Servidores disponibles:")
            for i, s in enumerate(servidores):
                print(f"{i+1}. {s.nombre}")

            try:
                origen = int(input("Seleccione servidor origen (número): ")) - 1
                destino = int(input("Seleccione servidor destino (número): ")) - 1

                if 0 <= origen < len(servidores) and 0 <= destino < len(servidores):
                    servidores[origen].conectar(servidores[destino])
                    print(f"Servidores '{servidores[origen].nombre}' y '{servidores[destino].nombre}' conectados.")
                else:
                    print("Selección inválida.")
            except ValueError:
                print("Debe ingresar un número válido.")

        
        elif opcion == "3":
            if not servidores:
                print("Primero cree un servidor.")
                continue

            email = input("Email: ")
            contrasena = input("Contraseña (6-12 caracteres): ")
            usuario = Usuario(email, contrasena)

            print("Servidores disponibles:")
            for i, s in enumerate(servidores):
                print(f"{i+1}. {s.nombre}")

            try:
                idx = int(input("Servidor destino (número): ")) - 1
                servidores[idx].registrar_usuario(usuario)
                usuarios[email] = usuario
                print(f"Usuario '{email}' registrado en {servidores[idx].nombre}.")
            except (ValueError, IndexError):
                print("Selección inválida.")

        
        elif opcion == "4":
            email = input("Email: ")
            if email in usuarios:
                usuario = usuarios[email]
                try:
                    if usuario.validar_contrasena():
                        # buscar servidor del usuario
                        servidor_usuario = next((s for s in servidores if usuario in s.usuarios), None)
                        if servidor_usuario:
                            menu_usuario(usuario, servidor_usuario)
                        else:
                            print("Error: el usuario no está asignado a ningún servidor.")
                    else:
                        print("Acceso denegado. Contraseña incorrecta.")
                except ValueError as e:
                    print("Error:", e)
            else:
                print("Usuario no encontrado.")

        
        elif opcion == "5":
            print(" CONEXIONES ENTRE SERVIDORES ")
            for s in servidores:
                conexiones = ", ".join(v.nombre for v in s.conexiones) if s.conexiones else "Sin conexiones"
                print(f"{s.nombre} -> {conexiones}")

        
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")
def menu_usuario(usuario, servidor):
    while True:
        print(f"\n--- MENÚ DE USUARIO: {usuario.mail()} ---")
        print("1. Enviar mensaje (mismo servidor)")
        print("2. Enviar mensaje por red (BFS)")
        print("3. Enviar mensaje por red (DFS)")
        print("4. Ver bandeja de entrada")
        print("5. Ver mensajes urgentes")
        print("6. Agregar filtro")
        print("7. Ver mensajes filtrados")
        print("8. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            destino_email = input("Email del destinatario: ")
            if destino_email in usuarios:
                destino = usuarios[destino_email]
                contenido = input("Contenido del mensaje: ")
                mensaje = Mensaje(usuario, destino, contenido)
                usuario.enviar_mensaje(mensaje)
                print("Mensaje enviado localmente.")
            else:
                print("Destinatario no encontrado.")

        elif opcion == "2" or opcion == "3":
            destino_email = input("Email del destinatario: ")
            if destino_email in usuarios:
                destino = usuarios[destino_email]
                contenido = input("Contenido del mensaje: ")
                mensaje = Mensaje(usuario, destino, contenido)

                origen_servidor = next((s for s in servidores if usuario in s.usuarios), None)
                destino_servidor = next((s for s in servidores if destino in s.usuarios), None)

                if not origen_servidor or not destino_servidor:
                    print("Error: servidores no asignados correctamente.")
                    continue

                if opcion == "2":
                    origen_servidor.enviar_bfs(destino_servidor, mensaje)
                else:
                    origen_servidor.enviar_dfs(destino_servidor, mensaje)
            else:
                print("Destinatario no encontrado.")

        elif opcion == "4":
            print("\n--- BANDEJA DE ENTRADA ---")
            for m in usuario.listar_mensajes():
                print(f"De: {m.remitente.mail()} | Contenido: {m.contenido}")

        elif opcion == "5":
            print("\n--- MENSAJES URGENTES ---")
            usuario.ver_urgentes()

        elif opcion == "6":
            clave = input("Ingrese palabra clave para filtrar: ")
            usuario.agregar_filtro(clave)
            print(f"Filtro '{clave}' agregado.")

        elif opcion == "7":
            usuario.ver_filtros()

        elif opcion == "8":
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")
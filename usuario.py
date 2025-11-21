from gestion import gestion

class Usuario(gestion):
    def __init__(self, email, contrasena):
        self._email = email
        self._contrasena = contrasena
        self.bandeja = []          
        self.filtros = {}           
        self.urgentes = []         

    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Bienvenido al sistema de correo")
            return func(*args, **kwargs)
        return wrapper

    @decorator
    def mail(self):
        return self._email

    def validar_contrasena(self):
        intentos = 3
        for i in range(intentos):
            entrada = input("Ingrese la contraseña (6-12 caracteres): ")

            if len(entrada) < 6:
                raise ValueError("La contraseña debe tener al menos 6 caracteres.")

            if 6 <= len(entrada) <= 12 and entrada == self._contrasena:
                print("Contraseña aceptada.")
                return True
            else:
                print(f"Contraseña inválida. Intento {i+1} de {intentos}")

        print("No se ingresó una contraseña válida.")
        return False

    def agregar_filtro(self, palabra_clave):
        if palabra_clave not in self.filtros:
            self.filtros[palabra_clave] = []
            print(f"Filtro agregado para la palabra: '{palabra_clave}'") #agrega una nueva palabra clave al diccionario de filtros
        else:
            print("Ese filtro ya existe.") #evita agregar filtros duplicados

    def enviar_mensaje(self, mensaje):
        contenido = mensaje.contenido.lower()
        filtrado = False

        # Si el emisor tiene filtros, revisa si el mensaje los activa
        for clave in self.filtros:
            if clave in contenido:
                self.filtros[clave].append(mensaje)
                filtrado = True
                break

        # Si contiene "urgente"
        if "urgente" in contenido:
            self.urgentes.append(mensaje)

        # Si no se filtró, lo guarda en bandeja común del emisor
        if not filtrado:
            self.bandeja.append(mensaje)

        # Finalmente, entrega el mensaje al destinatario
        mensaje.destino.recibir_mensaje(mensaje)


    def recibir_mensaje(self, mensaje):
        contenido = mensaje.contenido.lower()
        filtrado = False

        # Si el receptor tiene un filtro activo
        for clave in self.filtros:
            if clave in contenido:
                self.filtros[clave].append(mensaje)
                filtrado = True
                break

        # Si contiene "urgente"
        if "urgente" in contenido:
            self.urgentes.append(mensaje)

        # Si no se filtró, se guarda en la bandeja normal
        if not filtrado:
            self.bandeja.append(mensaje)


    def listar_mensajes(self):
        return self.bandeja #retorna la lista de mensajes en la bandeja de entrada


    def ver_urgentes(self):
        if not self.urgentes:
            print("No hay mensajes urgentes.") #verifica si hay mensajes urgentes
        else:
            print("Mensajes URGENTES:") 
            for m in self.urgentes:
                print(f" De: {m.remitente.mail()} | Mensaje : {m.contenido}") #muestra los mensajes urgentes


    def ver_filtros(self):
        if not self.filtros:
            print("(No hay filtros definidos)") 
            return

        for clave, mensajes in self.filtros.items():
            print(f"\nCategoría: '{clave}'")
            if mensajes:
                for m in mensajes:
                    print(f"  De: {m.remitente.mail()} | Mensaje: {m.contenido}")
            else:
                print("  (sin mensajes)") #verifica si hay filtros definidos

from gestion import gestion

class Usuario(gestion):
    def __init__(self, email, contrasena):
        self._email = email
        self._contrasena = contrasena
        self.bandeja = []
        self.filtros = {} # Diccionario para filtros personalizados
        self.urgentes = []  # Cola de mensajes urgentes

    def decorator(func):
        def wrapper (*args, **kwargs):
            print("bienvendio al sistema de correo")
            resultado=func(*args,**kwargs)
            return resultado
        return wrapper
    @decorator
    def mail(self):
        return self._email #retorna el email del usuario con un decorador que imprime un mensaje de bienvenida

    def validar_contrasena(self):
        intentos = 3
        for i in range(intentos):
            entrada = input("Ingrese la contraseña (6-12 caracteres): ")
            if 6 <= len(entrada) <= 12:
                self._contrasena = entrada
                print("Contraseña aceptada.")
                break
            else:
                print(f"Contraseña inválida. Intento {i+1} de {intentos}")
        else:
            print("No se ingresó una contraseña válida.")
            #  se utiliza para validar la contraseña del usuario asegurando que sea con 3 intentos y que tenga entre 6 y 12 caracteres
    
    def agregar_filtro(self, clave):
        self.filtros[clave.lower()] = []  # Inicializa lista vacía para esa clave

    def enviar_mensaje(self, mensaje):
        contenido = mensaje.contenido.lower()

        
        filtrado = False #se inicializa filtro en falso 
        for clave in self.filtros:
            if clave in contenido:
                self.filtros[clave].append(mensaje)
                filtrado = True
                break
                # Si el mensaje coincide con un filtro, se agrega a la lista correspondiente

        # Cola de urgentes
        if "urgente" in contenido:
            self.urgentes.append(mensaje) # Agrega mensaje a la cola de urgentes

        # Si no se filtró, va a la bandeja común
        if not filtrado:
            self.bandeja.append(mensaje)

    def recibir_mensaje(self, mensaje):
        self.bandeja.append(mensaje)  #permite recibir mensaje y lo agrega a la bandeja de entrada

    def listar_mensajes(self):
        return self.bandeja #retorna todos los mensajes en la bandeja de entrada
    
    def ver_urgentes(self):
        for m in self.urgentes:
            print("Mensajes URGENTES:", m.contenido) # permite ver los mensajes urgentes de la bandeja de entrada usando una cola

    def ver_filtros(self):
        for clave in self.filtros:
            print(f"Categoria: {clave}")
            for mensaje in self.filtros[clave]:
                print(mensaje.contenido) #permite ver los mensajes filtrados por categoria
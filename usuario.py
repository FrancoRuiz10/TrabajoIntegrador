from gestion import gestion

class Usuario(gestion):
    def __init__(self, email, contrasena):
        self._email = email
        self._contrasena = contrasena
        self.bandeja = []

    @property
    def mail(self):
        return self._email #retorna el email del usuario

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

    def enviar_mensaje(self, mensaje):
        mensaje.destino.recibir_mensaje(mensaje) #permite enviar mensaje a la carpeta destino

    def recibir_mensaje(self, mensaje):
        self.bandeja.append(mensaje)  #permite recibir mensaje y lo agrega a la bandeja de entrada

    def listar_mensajes(self):
        return self.bandeja #retorna todos los mensajes en la bandeja de entrada
    
    def mensaje_importante(self):
        mensaje = self.bandeja.pop()  
        print("Procesando:", mensaje._contenido) #permite ver los mensajes importantes de la bandeja de entrada usando pop mediante pilas 

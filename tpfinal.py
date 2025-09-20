from abc import ABC, abstractmethod

class gestion(ABC):
    @abstractmethod
    def enviar_mensaje(self, mensaje):
        pass
    @abstractmethod
    def recibir_mensaje(self, mensaje):
        pass
    @abstractmethod
    def listar_mensajes(self):
        pass

class Usuario(gestion):
    
    def __init__(self,email,contrasena):
        self._email=email
        self._contrasena=contrasena
        self.bandeja=[]
    @property
    def mail(self):
        return self._email
    def contra(self):
        intentos = 3

        for i in range(intentos):
            self._contrasena = input("Ingrese la contraseña (6-12 caracteres): ")

            if 6 <= len(self._contrasena) <= 12:
                print("Contraseña aceptada.")
                break
            else:
                print(f" Contraseña inválida. Intento {i+1} de {intentos}")
        else:
            print(" No se ingresó una contraseña válida.")

    def enviar_mensaje(self, mensaje):
        mensaje.destino.recibir_mensaje(mensaje)
        
    def recibir_mensaje(self, mensaje):
        self.bandeja.append(mensaje)

class Mensaje:
    def __init__(self,remitente,destino,mensaje):
        self._remitente=remitente
        self._destino=destino
        self._mensaje=mensaje
        
    @property #property lo que hace es que sea un metodo de solo lectura nada mas
    def remitente(self):
        return self._remitente

    @property
    def destino(self):
        return self._destino

    @property
    def mensaje(self):
        return self._mensaje


class Carpeta(gestion):
    def __init__(self):
        self._mensajes=[]

    def agregar_mensaje(self,mensaje):
        self._mensajes.append(mensaje)
    
    def listar_mensajes(self):
        return self._mensajes
    

class Servidorcorreo:
    def __init__(self):
        self.usuarios=[]
    
    def registrar_usuario(self,usuario):
        self.usuarios.append(usuario)
    
    def enviar_mensaje(self,mensaje):
        mensaje.destino.recibir_mensaje(mensaje)


from gestion import gestion

class Carpeta(gestion):
    def __init__(self, nombre):
        self.nombre = nombre
        self._mensajes = []
        self.subcarpetas = []

    def agregar_subcarpeta(self, carpeta):
        self.subcarpetas.append(carpeta)  # Añade una subcarpeta al árbol

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)  # Inserta un mensaje en esta carpeta

    def recibir_mensaje(self, mensaje):
        self.agregar_mensaje(mensaje)  # Recibe y almacena el mensaje

    def enviar_mensaje(self, mensaje):
        if hasattr(mensaje, 'destino'):
            mensaje.destino.recibir_mensaje(mensaje)  # Envía el mensaje a la carpeta destino donde el hasattr verifica si el mensaje tiene atributo destino

    def listar_mensajes(self):
        return self._mensajes  # Retorna los mensajes almacenados en esta carpeta 

    def mostrar_estructura(self, nivel=0):
        indent = "  " * nivel
        print(f"{indent} nombre de la carpeta 📂 {self.nombre}")
        for mensaje in self._mensajes:
            print(f"{indent}  tus mensajes 📨  {mensaje.mensaje}")
        for subcarpeta in self.subcarpetas:
            subcarpeta.mostrar_estructura(nivel + 1)  # Recursividad para mostrar jerarquía

    def mover_mensaje(self, mensaje, carpeta_destino):
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)
            carpeta_destino.agregar_mensaje(mensaje)  # Mueve el mensaje a otra carpeta

    def buscar_mensajes(self, criterio):
        criterio = criterio.lower()
        resultados = [
            m for m in self._mensajes
            if criterio in m.mensaje.lower() or criterio in m.remitente.mail.lower()
        ]
        for subcarpeta in self.subcarpetas:
            resultados.extend(subcarpeta.buscar_mensajes(criterio))  # Búsqueda recursiva
        return resultados

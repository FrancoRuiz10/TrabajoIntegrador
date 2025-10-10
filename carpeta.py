from gestion import gestion

class Carpeta(gestion):
    def __init__(self):
        self._mensajes = []
        self.subcarpetas = []

    def agregar_subcarpeta(self, carpeta):
        self.subcarpetas.append(carpeta) #añade subcarpetas al arbol

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje) #insetar mensaje en la carpeta que se encuentra actualmente

    def recibir_mensaje(self, mensaje):
        self.agregar_mensaje(mensaje) #recibe el mensaje y lo agrega a la carpeta

    def enviar_mensaje(self, mensaje):
        mensaje.destino.recibir_mensaje(mensaje) #envia el mensaje a la carpeta destino

    def listar_mensajes(self):
        return self._mensajes #retorna todos los mensajes almacenados en la carpeta

    def estructura(self, nivel=0):
        for mensaje in self._mensajes:
            print((nivel + 1) + f"- {mensaje.mensaje}")
        for sub in self.subcarpetas:
            sub.mostrar_estructura(nivel + 1) #muetras la estructura jerarquica de las carpetas y subcarpetas usando la recusivdad para recorrer el arbol
    
    def mover_mensaje(self, mensaje, carpeta_destino):
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)
            carpeta_destino.agregar_mensaje(mensaje) #permite mover mensajes entre carpetas

    def buscar_mensajes(self, criterio):
        criterio = criterio.lower()
        resultados = [
            m for m in self._mensajes
            if criterio in m.mensaje.lower() or criterio in m.remitente.mail.lower()
        ]
        for subcarpeta in self.subcarpetas:
            resultados += subcarpeta.buscar_mensajes(criterio)
        return resultados #realiza una busqueda recursiva en el arbol de las carpetas buscando mensajes que coincidan con el criterio dado donde a lo ultimo retorna una lista con todos los mensajes que coinciden


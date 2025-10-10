class Mensaje:
    def __init__(self, remitente, destino, contenido):
        self._remitente = remitente
        self._destino = destino
        self._contenido = contenido

    @property
    def remitente(self): 
        return self._remitente #retorna el remitente del mensaje

    @property
    def destino(self):
        return self._destino #retorna el destino del mensaje

    @property
    def contenido(self):
        return self._contenido #retorna el contenido del mensaje

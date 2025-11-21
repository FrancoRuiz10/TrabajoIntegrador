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

    #son metodos abstactos que pide la consigna que se deben implementar en las clases que herenden de gestion

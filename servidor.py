from collections import deque

class ServidorCorreo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = [] 
        self.conexiones = []  # servidores conectados (aristas del grafo)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario) # agrega un nuevo usuario al servidor

    def conectar(self, otro_servidor):  
        if otro_servidor not in self.conexiones:
            self.conexiones.append(otro_servidor)
            otro_servidor.conexiones.append(self) # establece una conexion bidireccional entre los distintos servidores

    def enviar_mensaje(self, mensaje):
        mensaje.destino.recibir_mensaje(mensaje) #envía el mensaje al destinatario

    def enviar_bfs(self, destino_servidor, mensaje):
        visitados = set()
        cola = deque([self])

        while cola:
            actual = cola.popleft()
            print(f"Visitando servidor: {actual.nombre}") #muestra el servidor actual en la busqueda

            if actual == destino_servidor:
                print("Mensaje entregado ")
                destino_servidor.enviar_mensaje(mensaje) #envia el mensaje al destinatario
                return True

            visitados.add(actual)
            for persona in actual.conexiones:
                if persona not in visitados:
                    cola.append(persona) # Agrega el servidor conectado a la cola
        return False

    def enviar_dfs(self, destino_servidor, mensaje, visitados=None):
        if visitados is None:
            visitados = set() # Inicializa el conjunto de visitados en la primera llamada

        print(f"Visitando servidor: {self.nombre}")

        if self == destino_servidor:
            print("Mensaje entregado con DFS ")
            destino_servidor.enviar_mensaje(mensaje) 
            return True # Si se encuentra el servidor destino retorna verdadero

        visitados.add(self)
        for persona in self.conexiones:
            if persona not in visitados:
                if persona.enviar_dfs(destino_servidor, mensaje, visitados): 
                    return True # Llamada recursiva

        return False # Si no se encuentra el servidor destino retorna falso

    def enviar_mensaje(self, mensaje):
        mensaje.destino.recibir_mensaje(mensaje) #envia el mensaje al destinatario usando el metodo enviar mensaje del usuario
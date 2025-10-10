class ServidorCorreo:
    def __init__(self):
        self.usuarios = [] 

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario) #agrega un nuevo usuario al servidor

    def enviar_mensaje(self, mensaje):
        mensaje.destino.recibir_mensaje(mensaje) #envia el mensaje al destinatario usando el metodo enviar mensaje del usuario

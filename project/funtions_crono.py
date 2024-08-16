def connect(server_address):
    socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            print("Conectando...")
            socket_obj.connect(server_address)

            if socket_obj:
                print ("Conexion establecida con: "+str(server_address))
                return socket_obj
        except:
            print("Esperando conexion")
            time.sleep(1)
            
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error:
            print("Fallo cargar imagen")
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color)
        return image

import socket
import re
import time

#Expresion regular 
patron = re.compile(r"\*+.+\*")

class atletas():
    def __init__(self,Place,Line,Id ,Name,club,Time,py):
        self.puesto = Place
        self.pista = Line
        self.ide = Id
        self.nombre = Name
        self.club = club
        self.marca = Time

        self.s_puesto = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 40), self.puesto, 1,(0,0,0))
        self.s_pista = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 40), self.pista, 1,(0,0,0))
        self.s_nombre = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 35), self.nombre, 1,(0,0,0))
        self.s_club = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 22), self.club, 1,(0,0,0))
        self.s_marca = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 42), self.marca, 1,(0,0,0))

        self.s_Lrect = self.s_puesto.get_rect() #lugar
        self.s_Lrect.left = 10
        self.s_Lrect.top = py

        self.s_Prect = self.s_pista.get_rect() #pista
        self.s_Prect.left = 155
        self.s_Prect.top = py

        self.s_Crect = self.s_club.get_rect() #club
        self.s_Crect.left = 720
        self.s_Crect.top = py
        
        self.s_Nrect = self.s_nombre.get_rect() #nombre
        self.s_Nrect.left = 275
        self.s_Nrect.top = py
            
        
        self.s_Mrect = self.s_marca.get_rect() #marca
        self.s_Mrect.left = 1210
        self.s_Mrect.top = py


def conectar(server_address):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            print("...conectando")
            sock.connect(server_address)

            if sock:
                print ("Conexion establecida")
                return sock
        except:
            print("esperando conexion")
            time.sleep(1)

server_addres = '192.168.1.101',3030
        
sock = conectar(server_addres)
llegada = []
py = 20

while True:
    datos = str(sock.recv(5000))
    if datos:
        if 'Hora' in datos:
            print(patron.search(datos).group(0).split("*")[1])# mensaje de hora actual
        if 'Tiempo' in datos:
            print(datos)
        
    else:
        try:
            sock.close()
        except:
            pass
        sock = conectar(server_addres)
        tiempo = sock.recv(5000)

"""
        if 'resultados' in tiempo:
            datos = tiempo.strip().split("\n")
            titulo = datos[1].strip().split(",")[1]
            viento = datos[2].strip().split(",")[1]
            for x in range(3,11):
                corredor = datos[x].strip().split(",")[:6]
                llegada.append(atletas(corredor[0],corredor[1],corredor[2],corredor[3],corredor[4],corredor[5],py))
                py+=30
                #Place,Line,Id ,Name,club,Time
        else:
            print(tiempo)

            #for x in datos:
             #   print x.strip().split(",")[:6]
    """ 
        
            
        





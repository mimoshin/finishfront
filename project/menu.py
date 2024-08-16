import pygame
import sys
import funciones as F

#texto
# puesto,dorsal,pista,nombre,apellido,equipo,licencia,tiempo
# lugar,marca,pista,nombre,AN,club,region

##____Clases____##
class Atleta():
    def __init__(self,puesto,dorsal,pista,nombre,apellido,equipo,tiempo,px,py):
        self.lugar = puesto
        self.nombre = nombre+apellido
        self.tiempo = tiempo
        self.pista = pista
        self.club = equipo
        self.fuente = pygame.font.Font("arial.ttf", 30)
        self.s_nombre = pygame.font.Font.render(self.fuente, self.nombre, 1,(0,0,0))
        self.s_lugar = pygame.font.Font.render(self.fuente, self.lugar, 1,(0,0,0))
        self.s_pista = pygame.font.Font.render(self.fuente, self.pista, 1,(0,0,0))
        self.s_marca = pygame.font.Font.render(self.fuente, self.tiempo, 1,(0,0,0))
        self.s_club = pygame.font.Font.render(self.fuente, self.club, 1,(0,0,0))
        self.s_Nrect = self.s_nombre.get_rect()
        self.s_Lrect = self.s_lugar.get_rect()
        self.s_Prect = self.s_pista.get_rect()
        self.s_Mrect = self.s_marca.get_rect()
        self.s_Crect = self.s_club.get_rect()
        self.s_Nrect.left = px #inicio eje x 
        self.s_Nrect.top = py  #inicio eje y
        self.s_Lrect.left = 40
        self.s_Lrect.top = py
        self.s_Prect.left = 255
        self.s_Prect.top = py
        self.s_Mrect.left = 110
        self.s_Mrect.top = py
        self.s_Crect.left = 1000
        self.s_Crect.top = py
        
        #print self.s_Nrect
        #print self.s_Nrect.top,self.s_Nrect.left
        #print self.s_Nrect.centerx,self.s_Nrect.centery
        
def main():
    total = []
    iteracion = 0
    PX,PY=400,245
    titulo = None
    salida = None 
    fuente = pygame.font.Font("arial.ttf", 30)
    pantalla = pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
    fondo = F.cargar_Imagen("plantilla.png",False)
    reloj = pygame.time.Clock()
    salir = False
    try:
        archivo = open('C:\Lynx/Boys3000.lif','r')
        for linea in archivo.xreadlines():
            if iteracion == 0:
                aux = linea.strip().split(',')
                titulo =  pygame.font.Font.render(fuente, aux[3], 1,(255,255,255))
                salida = titulo.get_rect()
                salida.left = 488
                salida.top = 40
            elif iteracion <= 8:
                aux = linea.strip().split(',')
                #print 'Puesto {0} DORSAL {1} PISTA {2} NOMBRE {3} APELLIDO {4} CLUB {5} TIEMPO {6} '.format(aux[0],aux[1],aux[2],aux[3],aux[4],aux[5],aux[6])
                total.append(Atleta(aux[0],aux[1],aux[2],aux[3],aux[4],aux[5],aux[6],PX,PY))
                PY += 65
            iteracion += 1
    except:
        print 'fallo'
        
    while salir != True:
        reloj.tick(15)
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if eventos.type == pygame.KEYDOWN:
                if eventos.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
        pantalla.blit(fondo,(0,0))
        pantalla.blit(titulo,salida)
        for x in total:
            pantalla.blit(x.s_nombre,x.s_Nrect)
            pantalla.blit(x.s_lugar,x.s_Lrect)
            pantalla.blit(x.s_pista,x.s_Prect)
            pantalla.blit(x.s_marca,x.s_Mrect)
            pantalla.blit(x.s_club,x.s_Crect)
            
        pygame.display.update()
        
if __name__ == '__main__':
    pygame.init()
    main()
   



    

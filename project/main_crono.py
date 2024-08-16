#!/usr/bin/env python
# -*- coding: utf-8 -*-s

#Expresion regular 
#patron = re.compile(r"\*+.+\*")

import socket
import re
import pygame
import time
import sys

ip = '192.168.1.12'
port = 3000

server_addres = ip , port

def connection(server_address):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            print("...conectando")
            socket.setdefaulttimeout(1)
            sock.connect(server_address)
            sock.settimeout(0.0200)
            if sock:
                print (f"Conexion establecida: IP -> {ip} | PORT -> {port}")
                return sock
        except:
            print("esperando conexion")
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

def main():
    pygame.init()
    sock = connection(server_addres)
    fuente = pygame.font.Font("./config/arial.ttf", 30)
    baner_prueba,baner_tiempo = True,True
    pantalla = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
    
    img_crono = load_image("./img/BANNER CRONOMETRO-Valpo.png",True)
    img_no_oficial =  load_image("./img/banner no oficial.png",True)
    img_titulo = load_image("./img/banner_titulo-Valpo.png",True)
    no_oficial = load_image("./img/tiempo_no_oficial-Valpo.png",True)
    
    event_name = " "
    time = " "
    reloj = pygame.time.Clock()
    salir,TNF = False, False
    while salir == False:
        reloj.tick(15)
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                salir = True
                pygame.quit()
                sys.exit()
            if eventos.type == pygame.KEYDOWN:
                
                #Cerrar el programa
                if eventos.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                #Habilitar banner tiempo
                if eventos.key == pygame.K_c:
                    if baner_tiempo:
                        baner_tiempo = False
                    else:
                        baner_tiempo = True

                #Habilitar banner titulo prueba
                if eventos.key == pygame.K_t:
                    #archivo = open('titulo.txt','r')
                    #event_name = archivo.read()[11:-1]
                    #archivo.close()
                    event_name='probando'
                    if baner_prueba:
                        baner_prueba = False
                    else:
                        baner_prueba = True

                #Habilitar mensaje tiempo no oficial
                if eventos.key == pygame.K_n:
                    if TNF:
                        TNF = False
                    else:
                        TNF = True
        try:
            datos = sock.recv(9048)
            if not datos:
                sock = connection(server_addres)
            else:
                datos = datos.decode('utf-16')
                if 'Crono' in datos:
                    format = datos.strip().split('_')
                    time = format[1]
                    if time != '0.0':
                        #print(f"Tiempo ->  {time}")
                        pass
                if 'HORA' in datos:
                    pass
                elif 'No Oficial' in datos:
                    time = datos[14:-1]
                    TNF = True
                    print(time)
                else:
                    print("Else: ",datos.split('\n'))                
        except socket.timeout:
            pass
        except:
            time = " ** "
            event_name = " ** "
        
        titulo = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 70),event_name, 1,(0,0,0))
        
        pantalla.fill((0,255,0))
        
        if baner_tiempo:
            if TNF:
                tiempo_llegada = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 90),"Tiempo No oficial", 1,(0,0,0))
                pantalla.blit(no_oficial,(280,230)) #imagen del banner
                pantalla.blit(tiempo_llegada,(370,260)) # tiempo corriendo
                TNF = False
                
            tiempo = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 120),time, 1,(0,0,0))
            pantalla.blit(img_crono,(1100,850)) #baner del tiempo
            pantalla.blit(tiempo,(1300,900)) # tiempo corriendo
                
        if baner_prueba:
                pantalla.blit(img_titulo,(10,20)) #banner del titulo
                pantalla.blit(titulo,(55,70)) # titulo de la prueba
        pygame.display.update()
        datos = 0

main()


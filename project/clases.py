#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame,sys,os
import funciones as F

class Serie():
    def __init__(self,archivo):
        self.Atletas = []
        self.archivo = archivo
        print("La clase cargo este dato",self.archivo,"\n")
        self.fuente = pygame.font.Font("config/arial.ttf", 50)
        self.cargar_Datos(self.archivo)

    def actualizar(self):
        self.Atletas = []
        self.cargar_Datos(self.archivo)    
        
    def cargar_Datos(self,archivos):
        py = 142
        print("Se quiere leer el archico -> ",archivos,"\n")
        texto = open(archivos,'r')

        try:
            for datos in texto.readlines():
                try:
                    print("entra al try")
                    if ('Serie' in datos) or ('SERIE' in datos):
                        list_datos = datos.strip().split(',')
                        self.titulo = list_datos[3]
                        self.s_titulo = pygame.font.Font.render(self.fuente, self.titulo, 1,(0,0,0))
                        self.s_Trect = self.s_titulo.get_rect()
                        self.s_Trect.left = 100
                        self.s_Trect.top = 30
                        if 'Posta' in  self.titulo :
                            py = 135
                    else:
                        list_datos = datos.strip().split(',')
                        self.Atletas.append(Atleta(list_datos[0],list_datos[1],list_datos[2],list_datos[3],list_datos[4],list_datos[5],list_datos[6],py))
                        print("Entro al else")
                    py+=70
                except:
                    print("fallo")
                    pass
                    #print 'Se intento cargar lo siguiente: {0}'.format(datos)
            texto.close()
        except:
            pass
    
class Atleta():
    def __init__(self,puesto,ide,pista,apellido,nombre,club,marca,py):
        self.puesto = puesto
        self.ide = ide
        self.pista = pista
        self.nombre = nombre.strip().split(' ')[0]+' '+apellido.strip().split(' ')[0]
        self.marca = marca
        self.club = club
        self.fuente = pygame.font.Font("config/arial.ttf", 35)
        self.s_pista = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 40), self.pista, 1,(0,0,0))
        self.s_nombre = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 35), self.nombre, 1,(0,0,0))
        self.s_club = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 22), self.club, 1,(0,0,0))
        self.s_marca = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 42), self.marca, 1,(0,0,0))
        self.s_puesto = pygame.font.Font.render(pygame.font.Font("config/arial.ttf", 40), self.puesto, 1,(0,0,0))
        #self.s_puntaje = pygame.font.Font.render(self.fuente, str(9-int(self.puesto)), 1,(0,0,0))


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

        #self.s_PUrect = self.s_puntaje.get_rect() #puntaje
        #self.s_PUrect.left = 1150
        #self.s_PUrect.top = py



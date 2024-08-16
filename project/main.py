#!usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as pg
import clases as A
import funciones as F
import sys,os,time

class Menu:
    def __init__(self):
        self.LISTA_SERIES = []
        self.SERIE_ACTUAL = 0
        pg.init()
        self.pantalla = pg.display.set_mode((1366,768),pg.FULLSCREEN)
        self.fondo = F.cargar_Imagen("img/plantilla2.png",False)
        self.medioFondo = F.cargar_Imagen("img/fondo.png",False)
        self.posta = F.cargar_Imagen("img/posta.png",False)
        self.reloj = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        

    def nueva_Serie(self,texto):
        return A.Serie("C:\Lynx\OUTPUT/"+texto)
    
    def definir_Series(self):
        self.LISTA_SERIES = []
        archivos = F.listar_Archivos()
        self.TOTAL = len(archivos)
        for nume in range(self.TOTAL):
            self.LISTA_SERIES.append(self.nueva_Serie(archivos[nume]))
        self.SERIE_ACTUAL = 0
                                     
    def run(self):
        self.playing = True
        while self.playing:
            self.reloj.tick(15)
            self.events()
            self.texto()
            self.update()
           

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        pg.display.update()
        pass

    def texto(self):
        self.pantalla.blit(self.fondo,(0,0))
        paso = None
        try:
            if('3000' in self.LISTA_SERIES[self.SERIE_ACTUAL].titulo or '800' in self.LISTA_SERIES[self.SERIE_ACTUAL].titulo ):
                self.pantalla.blit(self.medioFondo,(0,0))
                paso = "medio"
            if('Posta' in self.LISTA_SERIES[self.SERIE_ACTUAL].titulo):
                self.pantalla.blit(self.posta,(0,0))
                paso = "posta"
            self.pantalla.blit(self.LISTA_SERIES[self.SERIE_ACTUAL].s_titulo,self.LISTA_SERIES[self.SERIE_ACTUAL].s_Trect)
        except:
            pass
        for atleta in self.LISTA_SERIES[self.SERIE_ACTUAL].Atletas:
            if paso == "medio":
                atleta.s_pista = pg.font.Font.render(pg.font.Font("config/arial.ttf", 40)," ", 1,(0,0,0))
                atleta.s_Nrect.left = 140
                atleta.s_Crect.left = 680
                
            if paso == "posta":
                atleta.s_nombre = pg.font.Font.render(pg.font.Font("config/arial.ttf", 40)," ", 1,(0,0,0))
                atleta.s_club = pg.font.Font.render(pg.font.Font("config/arial.ttf", 40),atleta.club, 1,(0,0,0))
                atleta.s_Crect.left = 360
                
            self.pantalla.blit(atleta.s_pista,atleta.s_Prect)    
            self.pantalla.blit(atleta.s_puesto,atleta.s_Lrect)
            self.pantalla.blit(atleta.s_nombre,atleta.s_Nrect)
            self.pantalla.blit(atleta.s_club,atleta.s_Crect)
            self.pantalla.blit(atleta.s_marca,atleta.s_Mrect)
            

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    if self.SERIE_ACTUAL > 0:
                        self.SERIE_ACTUAL -= 1
                    else:
                        self.SERIE_ACTUAL = self.TOTAL-1
                        
                if event.key == pg.K_RIGHT:
                    if self.SERIE_ACTUAL < self.TOTAL-1:
                        self.SERIE_ACTUAL += 1
                    else:
                        self.SERIE_ACTUAL = 0
                if event.key == pg.K_a: #Actualizar serie actual
                    self.LISTA_SERIES[self.SERIE_ACTUAL].actualizar()
                if event.key == pg.K_r: #reingresar total de series
                    self.definir_Series()
    
    

# create the game object
g = Menu()
g.definir_Series()
while True:
    g.run()


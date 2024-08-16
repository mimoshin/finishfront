#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pygame as pg

def listar_Archivos():
    Archivos = []
    lista = os.listdir("C:\Lynx\OUTPUT\\")
    for indexi in lista:
        if "PENTATLON" in indexi:
            continue
        elif 'TETRATLON' in indexi:
            continue
        elif'HEXATLON' in indexi:
            continue
        elif 'CB' in indexi:
            continue
        elif '.lif' in indexi:
            Archivos.append(indexi)
    return Archivos

def cargar_Imagen(filename, transparent=False):
        try: imagen = pg.image.load(filename)
        except pg.error:
            print("Fallo cargar imagen")
        imagen = imagen.convert()
        if transparent:
                color = imagen.get_at((0,0))
                imagen.set_colorkey(color, RLEACCEL)
        return imagen




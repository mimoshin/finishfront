from tkinter import *
from tkinter import ttk
import socket

conection_address = '192.0.5.2',3030

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


sock = connect(conection_address)

mycolor = '#%02x%02x%02x' % (0, 255, 0)
raiz = Tk()
raiz.geometry('800x600')
raiz.configure(bg = mycolor)
raiz.title('finishLynx')
tinfo = Text(raiz,width = 40, height = 10)
tinfo.pack(side=TOP)               

ttk.Button(raiz,text='salir',command=quit).pack(side=BOTTOM)
raiz.mainloop()

binfo = ttk.Button(raiz,text='info')

while salir!=False:
    sock.recv(1000)
    print(sock.recv(1000))

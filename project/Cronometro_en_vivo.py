import socket,time
"""
    Conexion directa de mensajes
    Marcardor 
        **** Red lista, Puerto X -> server_addres debe ser igual a la ip de la maquina donde esta funcionando finishlynx
        y el puerto especificado en el marcador.
"""
categorias = {'INFANTIL':'INF','INTERMEDIA':'INTER','PREPARATORIA':'PREP','SUPERIOR':'SUP'}

ip = '192.168.1.12'
port = 3000

def conectar(server_address):
    #sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock = socket.socket()
    while True:
        try:
            print("...conectando")
            sock.connect(server_address)
            sock.settimeout(1)
            
            if sock:
                print (f"Conexion establecida: IP -> {ip} | PORT -> {port}")
                return sock
        except:
            print("esperando conexion")
            time.sleep(1)

def main():
    
    server_addres = ip , port
    sock = conectar(server_addres)

    while True:
        try:
            datos = sock.recv(9048)
            if not datos:
                sock = conectar(server_addres)
            else:
                datos = datos.decode('utf-16')
                if 'Crono' in datos:
                    format = datos.strip().split('_')
                    tiempo = format[1]
                    if tiempo != '0.0':
                        print(f"Tiempo ->  {tiempo}")
                else:
                    print(datos)
        except Exception as e:
            print(f"Error: {e}")

main()

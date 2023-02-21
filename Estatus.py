import socket, sys, os, time


def verificar(ip, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        status = sock.connect_ex((ip, puerto))
        if status == 0:
            print(f"Puerto: {port} - Abierto")
        else:
            print(f"Port: {port} - Cerrado")
            os.system("npm run dev --port={puerto}")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")    
        sys.exit()


if __name__ == '__main__':
    ip_address = "192.168.1.75"
    port = 5173
    url = "D:/6to semestre/ComputacionToleranteFallos/Codigos/persistenciaDatos/"
    
    os.chdir(url)
    while(True):
        verificar(ip_address, port)
        time.sleep(300)
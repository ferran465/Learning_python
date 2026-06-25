import socket

class crear_socket: 
    def __init__(self, port, ip):
        # creamos el objeto llamado socket_s y el puerto y ip  
        self.socket_s = socket.socket()
        # cojemos self.socket y le assignamos en memória a socket.socket que es donde se guardará
        self.port = port
        self.ip = ip
              

    def connect(self): 
        s = self.socket_s
        # assignamos s a self.socket para poderlo utilizar en connect
        s.connect((self.ip, self.port))

if __name__ == "__main__": 
    propio_socket = crear_socket(80, "192.168.1.34")
    propio_socket.connect()



            




        
import socket

class scan_port:
    def __init__(self, ip):
        self.ip = ip

        
    def scan(self): 
        for i in range(1, 65536):
            s = socket.socket()
            s.settimeout(0.1)
            
            try: 
                s.connect((self.ip, i))
                print("has been connected", i)

            except: 
                print("Hasn't been connected")


if __name__ == "__main__": 
    scan = scan_port("192.168.1.34")
    scan.scan()
            

     



        


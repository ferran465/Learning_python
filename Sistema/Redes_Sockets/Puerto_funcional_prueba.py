import socket

Conectado = "Has been succesfull"

No_Conectado = "Hasn't been conected"

def conectar():
	ip = str(input("Introduce una ip valida: "))
	for i in range(1, 65536):
		m = socket.socket()
		m.settimeout(0.01)

		try:
			m.connect((ip, i))
			print(Conectado, ip, i)
			
		except:
			print(No_Conectado, ip, i)
			
conectar()

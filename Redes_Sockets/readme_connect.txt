"""
Conéctese a un servicio TCP escuchando en la dirección de Internet (una tupla de 2 ), y devuelve el objeto de socket.
Este es un nivel superior función que: si el host es un nombre de host no numérico, Intentará resolverlo para ambos y , y luego intente conectarse a todas las direcciones posibles por turno hasta que la conexión tiene éxito.
Esto hace que sea fácil escribir clientes que lo sean compatible tanto con IPv4 como con IPv6.(host, port)socket.connect()

"""
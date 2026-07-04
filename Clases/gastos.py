class mis_gastos: 
    def __init__(self):
        pass 

    def calcular_gastos(self):
        que_ha_cobrado_este_mes = int(input("Introduce que ha cobrado este mes: "))
        self.agua = int(input("Introduce el gasto del agua de este mes: "))
        self.luz = int(input("Introduce el gasto de la luz de este mes: "))
        self.gas = int(input("Introduce el gasto del gas de este mes: "))
        self.casa = int(input("Introduce el gasto de la casa de este mes: "))


# Regla para decidir entre self.atributo y variable local:
# - self.algo -> cuando el dato debe sobrevivir entre distintos métodos
#   (representa el estado real del objeto, o lo necesita otro método más tarde)
# - variable local -> cuando el dato solo se usa dentro del mismo método,
#   como un paso intermedio de cálculo que no le importa a nadie fuera de ahí
# Abusar de self en todo contamina el objeto con datos temporales
# y puede generar bugs si un valor "viejo" se queda guardado sin querer.
            
        gastos = (self.agua + self.luz + self.gas + self.casa)

        que_ha_quedado_este_mes = gastos - que_ha_cobrado_este_mes

        print(gastos)
        print("Estos són tus gastos")
        print(que_ha_quedado_este_mes)
        print("Esto es lo que te queda")
        

objeto = mis_gastos()
objeto.calcular_gastos()


        
    
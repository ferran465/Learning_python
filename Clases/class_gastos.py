class mis_gastos: 
    def __init__(self):
        pass 

    def calcular_gastos(self):
        while True:
            try:
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

                extra = int(input("introduce un número de cuantos gástos quieres añadir: "))
                self.gasto_extra = []
                for i in range(extra):
                    descripción = str(input("Introduce la descripción del gasto: "))
                    importe = int(input("Introduce el importe: "))
                    self.gasto_extra.append({"descripción": descripción, "importe": importe})
                    
            except ValueError as e:
                print("Este número no és válido")
                return e
            
            pass
            break


        total_extra = sum(i["importe"] for i in self.gasto_extra)
        # hacemos una variable para sumar con i solo el importe al recorrer la lista de i;
        # porque solo queremos el número ya que si no, no puedes operar un diccionario con un entero o mejor dicho no se pueden operar diferentes tipados al recorrer la lista de i
        gastos = (self.agua + self.luz + self.gas + self.casa + total_extra)
        # Python no obliga a usar las variables o atributos que creas.
        # Puedes calcular self.gasto_extra, guardarlo, y nunca usarlo después:
        # el programa se ejecuta igual, sin error ni aviso.
        # Eso NO significa que esté bien - solo significa que Python
        # no comprueba si el resultado final es el que realmente querías.

        que_ha_quedado_este_mes = gastos - que_ha_cobrado_este_mes

        

        print("Estos són tus gastos")
        print(gastos)
        
    

        print("Esto es lo que te queda: ")
        print(que_ha_quedado_este_mes)

        


if __name__ == "__main__":
    objeto = mis_gastos()
    objeto.calcular_gastos()

def sumar(a:int, b:int) -> int:

    a = 10

    b = 20

    return a + b
print(sumar("a", "b"))

# Los typehints són una forma de decirle a python que esos valores tienen un tipado ya pueden ser (strings, bool, int, float etc...) pero hay un problema y es que python internamente eso le da igual puedes pasarle un string como en mi programa y lo deja pasar.

# -> es para declarar y sirve para mostrar errores más ubicables y que no te cueste de leer.
from classe_sumar_10 import sumar_10
from classe_restar_10 import restar_10

def operaciones_10(r, s):
    if r.restar > s.sumar: 
        return r.restar,s.sumar
    else: 
        if s.sumar > r.restar:
            return s.sumar,r.restar
        
r = restar_10(-10)
s = sumar_10(+10)

print(operaciones_10(r, s))
print(__name__)
        
class método(): 
    def __init__(self, método1, método2, método3):
        self.método1 = método1
        self.método2 = método2
        self.método3 = método3
        print("metodos"[:3]) & print("metodos"[:4])

    def __str__(self): 
        return f"Esto són los métodos{self.método1, self.método2, self.método3}"
        
m = método(1, 2, 3)
print(m)


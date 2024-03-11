

class Palindromos():
    def __init__(self,palabras):
        self.palabras=palabras
    def get_palabras(self): 
        return self.palabras
    def set_palabras(self, palabras):
        self.palabras=palabras
    def esPalindromo(self):
        palabras = self.palabras.replace(' ','').lower()
        return palabras==palabras[::-1]
    def resultado(self):
        if self.esPalindromo():
            return f'la palabra es {self.palabras} un palindromo' # f '' es para el formato
        else:
            return f'La palabra {self.palabras} no es un palindromo'
    
    def __str__(self):
        return self.resultado

def main():
    palabras = input('Escribe palabra:')
    palindromo=Palindromos(palabras)
    print(palindromo)

if __name__=="main":
    main()
    



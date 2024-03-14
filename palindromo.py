

class Palindromos():
    def __init__(self,palabras):
        self.palabras=palabras
    def get_palabras(self): 
        return self.palabras
    def set_palabras(self, palabras):
        self.palabras=palabras
    '''Funcion que nos da un booleano deciendo si se cumple o no'''
    def esPalindromo(self):
        palabras = self.palabras.replace(' ','').lower()
        return palabras==palabras[::-1]
    '''Devuelve el resultado de si es un palindromo con el formato string del atributo'''
    def resultado(self):
        if self.esPalindromo():
            return f'la palabra es {self.palabras} un palindromo'
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
    



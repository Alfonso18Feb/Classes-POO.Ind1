


class puzzle():
    '''constructor con el atributo que es el mensaje'''
    def __init__(self,mensaje):
        self.mensaje=mensaje
    #setters y gettes porque el mensaje puede cambiar
    def get_mensaje(self):
        return self.mensaje
    def set_mesaje(self,mensaje):
        self.mensaje=mensaje
        '''Esta función lo que hace es cambiar los mensajes escritos que no se entiendan y los cambia a un formato que se entienda y lo escrib en lower case'''
    def decodification(self,mensaje):
        self.mensaje=mensaje.replace('c','d').lower()
        self.mensaje=mensaje.replace('z','a').lower()
        self.mensaje=mensaje.replace('y','i').lower()
        self.mensaje=mensaje.replace('a','e').lower()
        self.mensaje=mensaje.replace('ç','c').lower()
        self.mensaje=mensaje.replace('.','o').lower()
        self.mensaje=mensaje.replace(',','r').lower()
        '''la función __str__'''
    def __str__(self,mensaje):
        return f'Mensaje:\n{mensaje}'

def main():
    incognita=input(str('Escribe su mensaje:\n'))
    cod=puzzle(incognita)
    print(cod)

if __name__=='__main__':
    main()


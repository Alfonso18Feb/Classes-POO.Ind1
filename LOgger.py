
class logger():
    '''constructor que tiene atributo del mensaje que quieres mandar y el numero de veces que llamamos a el metodo log que es LOGE'''
    def __init__(self,mensaje,loge):
        self.mensaje=mensaje
        self.loge=loge
    
    def get_mensaje(self):
        return self.mensaje
    def get_log(self):
        return self.loge
    #podemos cambiar el mensaje que queremos cambiar entonces ponemos un setter
    def set_mensaje(self,mensaje):
        self.mensaje=mensaje
    '''este metodo log crea un archivo Llamadas.txt podiendo escribirlo luego escrive star log 
    y empieza a escribir por cada linea un mensaje mandado y luego añade a +1 al loge'''
    def log(self,mensaje):
        file=open('Llamadas.txt',"w")
        file.write("--Start log--\n")
        file.writelines(self.mensaje)
        file.write("\n",self.mensaje)
        self.loge += 1
        '''Este metodo abre otravez el arch.txt y escribe los nºde vezes que llamas a log'''
    def log_end(self,):
        file = open('Llamadas.txt', 'w')
        file.write("--End log: {} log(s)--\n".format(self.loge))
        file.close()
'''Funcion main que pregunta cada vez si quieres escribir mas mensajes y cada vez se pasa a log'''
def main():
    pregunta=True
    while pregunta:
        mensaje=input("Escribe su mensaje:\n")
        s=input('quieres escribir otro mensaje:\n S o N:')
        if s=='s' or s=='S':
            mensaje=input("Escribe otro mensaje:\n")
            s=input('quieres escribir otro mensaje:\n S o N:')
        else:
            pregunta=False   
    loging=logger(mensaje)
    file=open('Llamadas.txt','r+')
    file.close


if __name__=="main":
    main()
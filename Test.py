


from LOgger import logger
'''importo la clase logger y esta classe tiene en comun el atributo loge'''
class test(logger):
    '''metodo llamada dice el numero de llamada o mensaje que estas'''
    def llamadas(self):
        return 'nº{} llamada'.format(self.loge)
def main():
    #ponemos loge=1 porque o si no empieza de 0 a infinito
    testing=test(loge=0)
    print(testing)
#Exercício - Abajur
#Nosso abajur tem apenas uma lâmpada e um único botão que é multifuncional. Quando tocado uma vez, acende a lâmpada com intensidade fraca. 
# Quando tocado pela segunda vez, acende a lâmpada com intensidade média. Quando tocado pela terceira vez, acende a lâmpada com intensidade forte.
#  E quando tocado pela quarta vez apaga a lâmpada. Sempre nesta sequencia de toques.

#Crie uma classe Abajur com os seguintes atributos de instância: lampada e intensidade. 
#O atributo lampada deve ser boleano (True/False). Na instância, o atributo lâmpada é setado em False. 
#O atributo intensidade deverá ser inteiro e assumir os valores 0, 1, 2, 3. Na instância este atributo (intensidade) é setado em 0.
#Os atributos devem ser todos privados, e para acessá-los implemente os seguintes métodos:
#Crie um método privado chamado liga_desliga_lampada. Neste método verifique se a intensidade for zero, o atributo lampada deve receber False (lâmpada apagada).
#  Caso contrário, lampada deve receber True (lâmpada acesa).

#A lâmpada estará apagada quando a intensidade for zero, e acessa para os outros valores 1,2,3.
#Crie um método privado chamado controla_intensidade. Este método deve sempre incrementar 1 no atributo intensidade.
#Quando o atributo intensidade for 4 este deve ser setado novamente em 0.

#Crie um método público chamado tocar_botao(). Este método vai simular o toque no botão. 
#Crie um método público chamado mostrar_status(). Este método deverá imprimir na tela os atributos para monitorarmos os seus conteúdos.
#Crie um método público chamado acoes, este vai chamar os métodos: controla_intensidade, liga_desliga_lampada e o mostrar_status.

#Para cada toque do botão, chame o método acoes, para ir acompanhando o que acontece em cada toque.

#-Crie uma instância de Abajur, e controle o tocar o botão para ligar a lâmpada e controlar a luminosidade.

#A cada toque no botão, o atributo intensidade será incrementado em 1. Variando de 0 a 3, onde: 0, significa luz apagada. 1, significa luz fraca. 2, significa luz média. 3, significa luz forte.

#+ tocar_no_botao().  Este método vai simular o botão, e deverá incrementar o atributo intensidade e alterar o conteúdo de lampada, se for o caso. 
#+ mostrar_status(). Este método deverá imprimir se a lâmpada está acessa ou apagada e qual a intensidade da luz.


class Abajur:
    """
    esss class estancia os atributos, lampada e intencidade
    """ 
    def __init__(self):
        self.__intensidade = 0
        self.__lampada = False 

    def __liga_desliga_lampada(self):
        if self.__intensidade == 0:
            self.__lampada = False
        else:
            self.__lampada =  True
        
    def __controla_intensidade(self):
        self.__intensidade += 1
        if self.__intensidade == 4:
            self.__intensidade = 0 
    
    def tocar_botao(self):
        self.__liga_desliga_lampada()
        self.__controla_intensidade()

    def mostrar_status(self):
        if self.__lampada:
            intensidade_str = {1:"baixa", 2:"media", 3:"alta"}[self.__intensidade]
            print(F"A lampada esta ligada com a intecidade {intensidade_str}")
        else:
            print("lampada esta desligada")
        

    def acoes(self):
        self.tocar_botao()
        self.mostrar_status()

    pass

def menu():
    abajur = Abajur()
    while True:
            print("\n MENU ")
            print("1. tocar no botão ")
            print("2. exibir status ")
            print("3. sair ")

            opcoes = input("escolha umas da opções: ")

            if opcoes == '1':
                abajur.acoes()
            elif opcoes =='2':
                abajur.mostrar_status()
            elif opcoes =='3':
                print("saido do programa!")
                break
            else:
                print("opção invalida, tente novamente" )
menu()



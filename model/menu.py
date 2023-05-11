
from controller.divisão import divisão
from controller.Soma import soma
from controller.multiplicacao import multiplicação
from controller.Subtracao import subtração


def menu ():
    teste = "sim"
    while teste == "sim":
        var = input('Digite qual operacao deseja fazer divisao, soma, multplicação, subtração >>>')

        if var == "divisao":

            n1 = int(input("digite um numero "))
            n2 = int(input("digite um numero "))
            print("o resultado é ",divisão(n1, n2))

        elif var== "soma":
            n1 = int(input("digite um numero"))
            n2 = int(input("digite um numero"))
            print("o resultado é >> " ,soma(n1, n2))
        elif var== "multiplicação":
            n1 = int(input("digite um numero"))
            n2 = int(input("digite um numero"))
            print("o resultado é >>" ,multiplicação(n1, n2)) 
        elif var== "subtração":
            n1 = int(input("digite um numero"))
            n2 = int(input("digite um numero"))
            print("o resultado é >> " ,subtração(n1, n2)) 


        teste = input("deseja continuar?")

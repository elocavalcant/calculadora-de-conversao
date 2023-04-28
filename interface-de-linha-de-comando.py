from calculadora import converterStringParaFloat, bitParaByte,byteParaBit,byteParaKB,KBParaByte,KBParaMB,MBParaKB,MBParaGB,GBParaMB,GBParaTB,TBParaGB,TBParaPB,PBParaTB

print (' Digite 1 para bitParaByte \n Digite 2 para byteParaBit \n Digite 3 para byteParaKB \n Digite 4 para KBParaByte \n Digite 5 para KBParaMB \n Digite 6 para MBParaKB \n Digite 7 para MBParaGB \n Digite 8 para GBParaMB \n Digite 9 Para GBParaTB \n Digite 10 para TBParaGB \n Digite 11 para TBParaPB \n Digite 12 para PBParaTB \n ')
funcEscolha = input()
if(funcEscolha == '1'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = byteParaBit (entradaDoTecladoValorASerConvertido)
    print (valorConvertido)

elif(funcEscolha == '3'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = byteParaKB (entradaDoTecladoValorASerConvertido)
    print (valorConvertido)

elif(funcEscolha == '4'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = KBParaByte (entradaDoTecladoValorASerConvertido)
    print (valorConvertido)

elif(funcEscolha == '5'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = KBParaMB (entradaDoTecladoValorASerConvertido)
    print (valorConvertido)     

elif(funcEscolha == '6'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = MBParaKB (entradaDoTecladoValorASerConvertido)
    print (valorConvertido)

elif(funcEscolha == '7'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = MBParaGB (entradaDoTecladoValorASerConvertido)
    print (valorConvertido)

elif(funcEscolha == '8'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = GBParaMB (entradaDoTecladoValorASerConvertido)
    print (valorConvertido)    

elif(funcEscolha == '9'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = GBParaTB (entradaDoTecladoValorASerConvertido)
    print (valorConvertido)

elif(funcEscolha == '10'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = TBParaGB (entradaDoTecladoValorASerConvertido)
    print (valorConvertido)

elif(funcEscolha == '11'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = TBParaPB (entradaDoTecladoValorASerConvertido)
    print (valorConvertido)

elif(funcEscolha == '12'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = PBParaTB (entradaDoTecladoValorASerConvertido)
    print (valorConvertido)


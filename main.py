from operadora import *

cont = 0

op = Operadora()

while(cont == 0):
    print("\nSeja bem-vindo ao JRango!")
    print("O que deseja fazer?")
    print("1 - Cadastrar cartão")
    print("2 - Cadastrar restaurante")
    print("3 - Acrescentar créditos")
    print("4 - Realizar pagamento")
    print("5 - Listar cartões")
    print("6 - Listar restaurantes")
    print("7 - Restaurante mais frequentado")
    print("9 - Sair")
    option = int(input())
    if option == 9:
        cont = 1
    else:
        if option == 1:
            op.cadastroCartao()
        elif option == 2:
            op.cadastroRestaurante()
        elif option == 3:
            op.acrescentarCredito()
        elif option == 4:
            op.opPgto()
        elif option == 5:
            op.listarCartoes()
        elif option == 6:
            op.listarRestaurantes()
        elif option == 7:
            op.maisFrequentado()
        else:
            print("Opção inválida!")
